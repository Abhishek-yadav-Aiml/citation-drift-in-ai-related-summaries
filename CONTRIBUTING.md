# Contributing

Thank you for helping improve this research repository.

## Before opening a change
- Keep the root TF-IDF baseline and the separate AlignScore scaffold clearly distinguished.
- Do not describe lexical similarity as factual entailment or citation support.
- Keep evidence availability separate from support labels. Retrieval failure or inaccessible full text must never be silently converted to unsupported.
- Do not commit private data, credentials, restricted PDFs, or model weights.
- Record dataset/model versions, licenses, prompts, seeds, splits and exact commands for experiments.
- Preserve raw experiment outputs and document whether results were actually reproduced.

## Development checks
From the repository root:

    python -m pip install -r requirements.txt
    python -m pytest -q
    python scripts/run_baseline.py --input data/processed/sample_claim_evidence.jsonl --output /tmp/sample_predictions.csv

For the isolated AlignScore scaffold tests:

    cd alignscore_scaffold
    python -m pip install -r requirements-core.txt
    python -m pytest -q tests

The tests do not verify official AlignScore checkpoint loading or end-to-end inference.

## Data and annotation changes
Update the data dictionary and annotation guidelines when changing a field or label. Keep synthetic test examples explicitly synthetic. Do not replace original independent annotator labels with adjudicated labels.
