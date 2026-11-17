#!/usr/bin/env python3
"""Run the root TF-IDF similarity review baseline."""
import argparse
from collections import Counter
import json
import platform
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import pandas as pd
import sklearn
from citation_drift.data import load_jsonl
from citation_drift.baseline import add_baseline_fields


def main():
    parser = argparse.ArgumentParser(
        description="Run a TF-IDF lexical-similarity review signal (not support classification)."
    )
    parser.add_argument("--input", required=True, help="Input claim/evidence JSONL file.")
    parser.add_argument("--output", required=True, help="Output CSV path.")
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.15,
        help="Similarity review cutoff between 0 and 1; it is not a support threshold.",
    )
    args = parser.parse_args()

    rows = add_baseline_fields(load_jsonl(args.input), threshold=args.threshold)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(output, index=False)

    scored = sum(row["similarity_score"] is not None for row in rows)
    status_counts = dict(Counter(row["evidence_status"] for row in rows))
    metadata = {
        "baseline": "TF-IDF cosine similarity",
        "score_interpretation": "lexical review signal; not factual entailment or support",
        "similarity_review_cutoff": args.threshold,
        "input_path": str(Path(args.input)),
        "output_path": str(output),
        "n_records": len(rows),
        "n_scored": scored,
        "n_not_scored": len(rows) - scored,
        "evidence_status_counts": status_counts,
        "python_version": sys.version,
        "platform": platform.platform(),
        "scikit_learn_version": sklearn.__version__,
        "pandas_version": pd.__version__,
    }
    metadata_path = output.with_name(output.stem + ".metadata.json")
    metadata_path.write_text(json.dumps(metadata, indent=2), encoding="utf-8")

    print(f"Wrote {len(rows)} records to {output}")
    print(f"Scored: {scored}; not scored: {len(rows) - scored}")
    print(f"Run metadata: {metadata_path}")
    print("Similarity flags are for review only; they are not factual support labels.")


if __name__ == "__main__":
    main()
