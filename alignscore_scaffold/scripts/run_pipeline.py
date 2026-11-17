import argparse
import csv
import hashlib
import json
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
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", default="results/alignscore_predictions.csv")
    parser.add_argument("--checkpoint", required=True)
    parser.add_argument("--device", default="cpu")
    parser.add_argument("--batch-size", type=int, default=1)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--threshold", type=float, default=None)
    args = parser.parse_args()
    set_seed(args.seed)
    records, errors = load_jsonl(args.input)
    records = prepare_records(records)
    scorer = AlignScoreScorer(args.checkpoint, device=args.device, batch_size=args.batch_size)
    scores = scorer.score([r["evidence_processed"] for r in records],
                          [r["claim_processed"] for r in records])
    for row, value in zip(records, scores):
        row["alignscore"] = value
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    fields = ["example_id", "source_paper_id", "claim_id", "partition",
              "claim", "evidence", "alignscore", "gold_label"]
    with output.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(records)
    checkpoint = Path(args.checkpoint)
    metadata = {"python": sys.version, "platform": platform.platform(),
                "seed": args.seed, "device": args.device,
                "checkpoint_sha256": sha256(checkpoint),
                "n_records": len(records), "validation_errors": errors,
                "score_semantics": "continuous alignment score, not four-class labels"}
    Path("results").mkdir(exist_ok=True)
    Path("results/run_metadata.json").write_text(json.dumps(metadata, indent=2))
    save_score_histogram(scores, "results/score_distribution.png")
    if args.threshold is not None:
        metrics = evaluate_binary(records, args.threshold)
        Path("results/metrics.json").write_text(json.dumps(metrics, indent=2))
    print(f"Scored {len(records)} records; output: {output}")

if __name__ == "__main__":
    main()
