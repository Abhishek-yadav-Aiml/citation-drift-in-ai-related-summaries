# Detecting Citation Drift in AI-Generated Literature Summaries

Research repository for evaluating whether claims in AI-generated scientific literature summaries are supported by their cited source papers.

## Two distinct code paths

1. **Root project — TF-IDF baseline:** a lightweight lexical-similarity baseline in `src/citation_drift/`. Similarity is a review signal, not an entailment or truth classifier.
2. **`alignscore_scaffold/` — AlignScore research scaffold:** a separate continuous-score pipeline with BM25 helper, score export, metadata and a Colab starter notebook. End-to-end installation/inference has NOT been verified.

A third result is documented separately in `reports/preliminary_scifact_deberta_report.md`: a user-reported SciFact development-set experiment using `cross-encoder/nli-deberta-v3-base`. Do not conflate those NLI metrics with either repository baseline.

## Research questions

- For claims in AI-generated CS literature summaries, how does evidence context (abstract-only vs automatically retrieved full-text passages) affect claim-level citation-support evaluation?
- How much verification error is associated with retrieval failure, comparing BM25-retrieved evidence and human-selected evidence?

## Annotation policy

Support labels: `SUPPORTED`, `PARTIALLY_SUPPORTED`, `NOT_SUPPORTED_IN_INSPECTED_SOURCE`, `CONTRADICTED`.

Evidence availability is a separate field. An inaccessible or unretrieved paper is not proof that a claim is unsupported. See `docs/annotation_guidelines.md` and `alignscore_scaffold/configs/label_policy.md`.

## Quick start: root TF-IDF baseline

Python 3.10+ recommended.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest -q
python scripts/run_baseline.py --input data/processed/sample_claim_evidence.jsonl --output results/sample_predictions.csv
```

This lexical baseline is not a factual-entailment classifier. Synthetic examples are smoke-test fixtures, not scientific evidence.

## AlignScore scaffold

See `alignscore_scaffold/README.md`. It requires a compatible official AlignScore environment and checkpoint not bundled here. Its import, checkpoint loading, inference and tests remain TEST REQUIRED. The AlignScore output is a continuous score, not a validated four-class prediction.

## Repository layout

- `src/citation_drift/`: root TF-IDF baseline and data/evaluation utilities
- `scripts/`: root baseline command
- `tests/`: root tests
- `alignscore_scaffold/`: separate AlignScore pipeline, config, synthetic fixture, Colab notebook and tests
- `docs/`: research protocol, annotation, data dictionary and reproduction notes
- `reports/`: preliminary experiment report and template
- `paper/overleaf/`: IEEE conference LaTeX and BibTeX draft
- `prompts/`: fixed research prompt templates

## Reproducibility and limitations

No real research corpus or model checkpoint is bundled. Dataset release and redistribution terms must be checked at the official source. The separate SciFact/DeBERTa metrics are reported by the project author; its original executable notebook/script and raw outputs are not included here. AlignScore has not been reproduced end-to-end. Paper-level splitting is required to avoid leakage; thresholds must be selected on development data only and frozen before test evaluation.

## License and third-party materials

Review `LICENSE` and ensure it reflects the repository owner's intent. Third-party datasets, papers, model weights and software remain subject to their own terms. Do not upload credentials, restricted PDFs, private annotations or non-redistributable checkpoints. The `.gitignore` excludes common secrets, local environments, model weights, private datasets and generated outputs.
