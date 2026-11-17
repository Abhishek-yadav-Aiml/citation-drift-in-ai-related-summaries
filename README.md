# Detecting Citation Drift in AI-Generated Literature Summaries

Research repository for studying claim-level citation support in AI-generated scientific literature summaries.

## Research focus
This project investigates how evidence context (abstract-only versus retrieved full-text passages) affects citation-support assessment, and how retrieval failure can influence verification.

## Repository status
This repository contains a research scaffold and preliminary documentation. The AlignScore pipeline has **not** been verified end-to-end. The SciFact/DeBERTa experiment described in the report is a separate preliminary experiment; it must not be conflated with AlignScore results.

## Contents
- `src/citation_drift/`: data loading, preprocessing, retrieval helper, scoring adapter, evaluation and plotting utilities
- `scripts/run_pipeline.py`: pipeline entry point
- `notebooks/`: Colab-oriented workflow
- `configs/`: experiment settings and label policy
- `data/processed/sample_synthetic.jsonl`: synthetic examples for pipeline smoke tests only, not research data
- `docs/`: research decisions, annotation guidelines and validation report
- `reports/`: preliminary experiment report
- `paper/overleaf/`: IEEE-style LaTeX source and BibTeX references
- `prompts/`: prompt templates used during research workflow

## Important methodological distinctions
The annotation labels are `SUPPORTED`, `PARTIALLY_SUPPORTED`, `NOT_SUPPORTED_IN_INSPECTED_SOURCE`, and `CONTRADICTED`. Evidence availability is recorded separately. Inaccessible or unretrieved evidence must not be labelled as unsupported.

AlignScore produces a continuous alignment score; the current scaffold does not provide a validated four-class classifier. The DeBERTa NLI numbers in the preliminary report are from a separate SciFact development-set experiment.

## Setup
Use Python 3.10 in a clean environment. Install the core scaffold dependencies:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
python -m pip install --upgrade pip
pip install -r requirements-core.txt
```

AlignScore dependencies and checkpoint setup are not yet confirmed. Consult `AI_ASSISTANCE_DEBUGGING_LOG.md` and the validation report before attempting baseline inference. Do not assume that installing core dependencies is sufficient for AlignScore.

## Run tests

```bash
python -m pytest -q
```

This test command has not yet been confirmed in the target Colab environment; treat it as **TEST REQUIRED** until its output is recorded.

## Run the pipeline
After installing the required AlignScore dependencies and placing the authorized checkpoint at `models/AlignScore-base.ckpt`, prepare `data/processed/claim_evidence.jsonl` using the schema in the data module and run:

```bash
python scripts/run_pipeline.py \\
  --input data/processed/claim_evidence.jsonl \\
  --output results/alignscore_predictions.csv \\
  --checkpoint models/AlignScore-base.ckpt \\
  --device cpu --batch-size 1 --seed 42
```

**TEST REQUIRED:** the scaffold command, checkpoint compatibility, and end-to-end inference have not been successfully verified. The CLI currently does not parse `configs/experiment.yaml`; command-line arguments are the operative settings. BM25 helper code exists but is not wired as a `--use-bm25` CLI option.

## Data and licenses
No real research dataset is bundled. The included JSONL is synthetic. Verify the dataset's official version, license, access conditions and redistribution rules before downloading or sharing SciFact, CS-PaperSum, or other corpus files. Model checkpoint weights are not included. Check the upstream model/checkpoint license before use or redistribution.

## Reproducibility and reporting
Record Python and package versions, OS/runtime, device, checkpoint source and SHA-256, dataset version and license, split IDs, random seed, exact commands, and raw outputs. Keep paper-level grouping to prevent leakage. Select any threshold using development data only and freeze it before test evaluation.

## Limitations
- AlignScore installation and inference remain unverified.
- No real research dataset, model checkpoint, or generated predictions are included.
- The current AlignScore adapter is not a four-class classifier.
- BM25 helper is not integrated into the pipeline CLI.
- Configuration YAML is documentation at present; the script does not load it.
- No end-to-end reproduction or performance claim should be inferred from this scaffold.

## Citation and credits
See `paper/overleaf/references.bib` for the bibliography used by the draft, and the reports/docs for experiment-specific provenance. Cite original datasets and models according to their official instructions.

## License
No project-level open-source license is granted by this repository at present. Dataset, model and paper rights remain with their respective owners. Add an explicit project license only after deciding what you have rights to release.
