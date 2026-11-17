# AlignScore research scaffold

This is a separate experimental scaffold, retained alongside the root TF-IDF baseline. It is **not yet validated end-to-end**.

## Expected input
JSONL at data/processed/claim_evidence.jsonl, one object per line, with required fields example_id, source_paper_id, claim and evidence. Optional gold_label, claim_id and partition fields are used in outputs.

The bundled sample_synthetic.jsonl contains invented examples for schema smoke tests only.

## Setup
Use a dedicated Python 3.10 environment and install requirements-core.txt. AlignScore requires additional compatible dependencies and an authorized checkpoint; the core requirements file is not sufficient. Past Colab attempts reported missing spaCy and click modules. A successful import and inference are not confirmed.

## Intended command (TEST REQUIRED)
After verifying the official AlignScore installation and placing the authorized checkpoint at models/AlignScore-base.ckpt:

    python scripts/run_pipeline.py --input data/processed/claim_evidence.jsonl --output results/alignscore_predictions.csv --checkpoint models/AlignScore-base.ckpt --device cpu --batch-size 1 --seed 42

## Important
AlignScore returns a continuous score, not a validated four-class prediction. A binary threshold must be selected on development data and frozen before test. No model weights, real dataset or results are bundled. Check upstream license terms.
