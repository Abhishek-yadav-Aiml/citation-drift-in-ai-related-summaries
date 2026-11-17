# AlignScore research scaffold

This is an isolated, optional scoring scaffold. It is separate from the root TF-IDF baseline.

## What it does
- Validates JSONL claim/evidence records.
- Applies conservative whitespace normalization.
- Calls the official AlignScore package through a thin adapter.
- Exports continuous scores, run metadata (including checkpoint SHA-256), and a score histogram.
- Optionally calculates a declared binary evaluation on eligible gold labels.

**It does not train AlignScore. It does not produce a validated four-class classifier.** An AlignScore score is a continuous consistency signal and requires a development-set threshold for any binary analysis.

## Folder and paths
Run commands from inside `alignscore_scaffold/`. The checkpoint path is relative to this folder unless an absolute path is supplied. No checkpoint or research dataset is stored in Git. The bundled `data/processed/sample_synthetic.jsonl` is invented smoke-test data only. See the [input schema](data/processed/schema.json).

## Core scaffold tests
Python 3.10+ is recommended.

    python -m pip install -r requirements-core.txt
    python -m pytest -q tests

These dependencies cover the small scaffold tests, **not the full AlignScore installation**.

## Model installation and checkpoint
Install a compatible version of the upstream AlignScore package and its complete dependencies from its official project instructions. Check the checkpoint's provenance, license and compatibility with the installed code. Previous setup attempts in this project did not confirm a successful import; therefore no dependency combination is claimed to be validated here.

Place the authorized checkpoint at:

    alignscore_scaffold/models/AlignScore-base.ckpt

The model weights directory is git-ignored. Do not commit checkpoints or restricted files.

## Smoke-test command (TEST REQUIRED)
From this directory, after a compatible package and checkpoint are installed:

    python scripts/run_pipeline.py \
      --input data/processed/sample_synthetic.jsonl \
      --output results/sample_predictions.csv \
      --checkpoint models/AlignScore-base.ckpt \
      --device cpu --batch-size 1 --seed 42

This only tests wiring on synthetic examples. It is not a research evaluation.

## Real experiment input
Prepare a JSONL file under a licensed data location using the linked schema. Required fields are:
- `example_id`: unique example ID
- `source_paper_id`: stable paper grouping key
- `claim`: atomic claim text
- `evidence`: inspected evidence passage

Optional fields include `claim_id`, `partition` and `gold_label`. Do not submit inaccessible or unretrieved evidence to the scorer as empty text. Record its evidence-availability status in the annotation data and exclude it from scoring until valid evidence is available. See `configs/label_policy.md`.

## Optional binary metrics
If using `--threshold`, select it on development data only and freeze it before test. The default binary mapping includes only SUPPORTED (positive) and NOT_SUPPORTED_IN_INSPECTED_SOURCE (negative). Partial and contradicted cases are excluded from that binary calculation and must not be silently recoded.

For a previously selected development threshold, use an explicit development partition:

    python scripts/run_pipeline.py --input data/processed/your_dev.jsonl --output results/dev_predictions.csv --checkpoint models/AlignScore-base.ckpt --threshold "$DEV_THRESHOLD" --evaluation-partition dev

The script filters metric calculation to the requested partition; it does not choose a threshold for you.

## Current validation status
- JSONL/preprocessing/retrieval/evaluation helper tests are included.
- GitHub Actions runs scaffold unit tests separately from the root project.
- Official AlignScore installation, checkpoint loading and inference remain **TEST REQUIRED**.
- No real corpus, checkpoint, predictions or research results are bundled.
