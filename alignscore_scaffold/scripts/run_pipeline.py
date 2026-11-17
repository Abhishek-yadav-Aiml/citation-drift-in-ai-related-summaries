import argparse
import csv
import hashlib
import json
import math
import platform
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from citation_drift.seed import set_seed
from citation_drift.data import load_jsonl
from citation_drift.preprocess import prepare_records
from citation_drift.alignscore_model import AlignScoreScorer
from citation_drift.evaluate import evaluate_binary
from citation_drift.plots import save_score_histogram


def sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main():
    parser = argparse.ArgumentParser(
        description="Score claim/evidence pairs with the official AlignScore package."
    )
    parser.add_argument("--input", required=True, help="Input JSONL file.")
    parser.add_argument("--output", default="results/alignscore_predictions.csv")
    parser.add_argument("--checkpoint", required=True)
    parser.add_argument("--device", default="cpu")
    parser.add_argument("--batch-size", type=int, default=1)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument(
        "--threshold", type=float, default=None,
        help="Optional binary threshold. Metrics are calculated only on --evaluation-partition."
    )
    parser.add_argument("--evaluation-partition", default="dev")
    parser.add_argument("--positive-label", default="SUPPORTED")
    parser.add_argument(
        "--negative-labels", nargs="*",
        default=["NOT_SUPPORTED_IN_INSPECTED_SOURCE"]
    )
    args = parser.parse_args()

    if args.batch_size < 1:
        parser.error("--batch-size must be at least 1")
    if args.threshold is not None and not math.isfinite(args.threshold):
        parser.error("--threshold must be finite")

    set_seed(args.seed)
    records, errors = load_jsonl(args.input)
    records = prepare_records(records)

    scorer = AlignScoreScorer(
        args.checkpoint, device=args.device, batch_size=args.batch_size
    )
    scores = scorer.score(
        [row["evidence_processed"] for row in records],
        [row["claim_processed"] for row in records],
    )
    for row, value in zip(records, scores):
        row["alignscore"] = value

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "example_id", "source_paper_id", "claim_id", "partition",
        "claim", "evidence", "alignscore", "gold_label",
    ]
    with output.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(records)

    checkpoint = Path(args.checkpoint)
    metadata = {
        "python": sys.version,
        "platform": platform.platform(),
        "seed": args.seed,
        "device": args.device,
        "batch_size": args.batch_size,
        "checkpoint_path": str(checkpoint),
        "checkpoint_sha256": sha256(checkpoint),
        "input_path": str(Path(args.input)),
        "n_records": len(records),
        "validation_errors": errors,
        "score_semantics": "continuous alignment score; not a four-class classification",
        "threshold": args.threshold,
        "evaluation_partition": args.evaluation_partition if args.threshold is not None else None,
    }
    results_dir = output.parent
    (results_dir / "run_metadata.json").write_text(
        json.dumps(metadata, indent=2), encoding="utf-8"
    )
    save_score_histogram(scores, results_dir / "score_distribution.png")

    if args.threshold is not None:
        evaluation_records = [
            row for row in records
            if str(row.get("partition", "")).lower()
            == args.evaluation_partition.lower()
        ]
        if not evaluation_records:
            raise ValueError(
                f"No records found for evaluation partition "
                f"{args.evaluation_partition!r}. Threshold evaluation is dev-only by default."
            )
        metrics = evaluate_binary(
            evaluation_records,
            args.threshold,
            positive_label=args.positive_label,
            negative_labels=tuple(args.negative_labels),
        )
        metrics["evaluation_partition"] = args.evaluation_partition
        (results_dir / "metrics.json").write_text(
            json.dumps(metrics, indent=2), encoding="utf-8"
        )
        print(
            f"Binary metrics saved for partition {args.evaluation_partition!r}. "
            "Ensure the threshold was selected on development data only."
        )

    print(f"Scored {len(records)} records.")
    print(f"Predictions: {output}")
    print(f"Metadata: {results_dir / 'run_metadata.json'}")
    print(f"Histogram: {results_dir / 'score_distribution.png'}")


if __name__ == "__main__":
    main()
