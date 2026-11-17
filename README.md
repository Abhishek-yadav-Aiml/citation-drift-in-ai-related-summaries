# Detecting Citation Drift in AI-Generated Literature Summaries

A reproducible research scaffold for auditing whether claims in AI-generated scientific literature summaries are supported by the cited papers.

## What this repository does
1. Stores summary claims with cited paper IDs and inspected evidence passages.
2. Records human support labels separately from evidence availability.
3. Runs a transparent TF-IDF cosine-similarity baseline (a retrieval/similarity signal, **not** a factual-entailment classifier).
4. Exports claim-level predictions and simple evaluation metrics when gold labels are supplied.

## Research safeguards
- Labels: `SUPPORTED`, `PARTIALLY_SUPPORTED`, `NOT_SUPPORTED_IN_INSPECTED_SOURCE`, `CONTRADICTED`.
- Evidence availability is separate. An inaccessible or unretrieved paper is **not** evidence that a claim is unsupported.
- Similarity scores do not establish entailment or truth. All automated scores require human review.
- Bundled examples are synthetic smoke-test data, not scientific findings.
- Split by paper, not individual claims, to avoid leakage.

## Quick start (Python 3.10+)
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest -q
python scripts/run_baseline.py --input data/processed/sample_claim_evidence.jsonl --output results/sample_predictions.csv
```

## Input format
One JSON object per line with `claim_id`, `summary_id`, `paper_id`, `claim`, `evidence`, and `evidence_status`. Optional `gold_label` can be supplied. See `docs/data_dictionary.md`.

## Layout
- `src/citation_drift/`: data loading, baseline scoring and evaluation
- `scripts/`: command-line entry point
- `data/processed/`: synthetic smoke-test examples
- `docs/`: annotation policy and experiment protocol
- `reports/`: report template
- `notebooks/`: starter notebook
- `tests/`: unit tests

## Current status
This is a starter implementation. No real corpus, trained model checkpoint, or validated research result is included. The TF-IDF baseline is intentionally simple and must be compared against human annotations. Add AlignScore/NLI only after verifying dependencies, checkpoint provenance, license and end-to-end execution.

## Research workflow
Define inclusion criteria; acquire a permitted corpus; generate and preserve summaries; segment atomic claims; map claims to cited papers; inspect source passages; annotate independently; adjudicate; run baselines; evaluate on paper-level splits; report class-wise metrics, macro-F1, coverage, agreement and uncertainty.

## License
See `LICENSE`. Third-party datasets, papers, models and tools remain subject to their own licenses.
