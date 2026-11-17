#!/usr/bin/env python3
import argparse
from pathlib import Path
import pandas as pd
from citation_drift.data import load_jsonl
from citation_drift.baseline import add_baseline_fields

def main():
    parser = argparse.ArgumentParser(description="Run lexical similarity baseline.")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--threshold", type=float, default=0.15)
    args = parser.parse_args()
    rows = add_baseline_fields(load_jsonl(args.input), threshold=args.threshold)
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(out, index=False)
    print(f"Wrote {len(rows)} rows to {out}")
    print("Similarity flags are not factual support labels.")

if __name__ == "__main__":
    main()
