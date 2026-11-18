# Detecting Citation Drift in AI-Generated Literature Summaries

[![Tests](https://github.com/Abhishek-yadav-Aiml/citation-drift-in-ai-related-summaries/actions/workflows/tests.yml/badge.svg)](https://github.com/Abhishek-yadav-Aiml/citation-drift-in-ai-related-summaries/actions/workflows/tests.yml)

A research codebase for examining whether factual claims in scientific literature summaries are supported by the papers cited for them.

## Repository scope

The repository currently contains two code paths:

1. **Root TF-IDF baseline** — a lightweight lexical-similarity review signal in `src/citation_drift/`. It flags claim/evidence text pairs for review. It does **not** predict whether a claim is true or supported.
2. **AlignScore scaffold** — an isolated optional pipeline in `alignscore_scaffold/` that calls the external AlignScore package and returns a continuous score. Its full model installation, checkpoint loading and end-to-end inference have not yet been verified.

The repository also contains an IEEE LaTeX draft, BibTeX references, a paper-access index, and a download script for three ACL papers whose reuse terms are explicit. Two DeBERTa papers are linked to their official hosts rather than mirrored because their individual redistribution licenses were not confirmed.

## Research questions in the protocol

- For claims in AI-generated computer-science literature summaries, how does evidence context (abstract-only versus retrieved full-text passages) affect claim-level citation-support assessment?
- How should retrieval failure and inaccessible evidence be separated from genuinely unsupported or contradicted claims?

See [research decisions](docs/research_decisions.md), [experiment protocol](docs/experiment_protocol.md), [annotation guidelines](docs/annotation_guidelines.md), and the [pilot annotation specification](docs/annotation_guideline_pilot_spec.md).

## Evidence and annotation policy

Support labels:
- `SUPPORTED`
- `PARTIALLY_SUPPORTED`
- `NOT_SUPPORTED_IN_INSPECTED_SOURCE`
- `CONTRADICTED`

Evidence availability is a separate field:
- `available`
- `not_retrieved`
- `inaccessible`
- `not_provided`

An inaccessible or unretrieved paper is not evidence that a claim is unsupported. Exact schema details are in [data_dictionary.md](docs/data_dictionary.md) and [schema.json](data/processed/schema.json).

## Quick start: root TF-IDF review baseline

Python 3.10 or newer is recommended.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pytest -q
python scripts/run_baseline.py \
  --input data/processed/sample_claim_evidence.jsonl \
  --output results/sample_predictions.csv
```

The sample file contains five invented examples for software checks only. It is not research data. Records with unavailable evidence are deliberately not scored. The default similarity cutoff (0.15) is a configurable review heuristic, not a validated decision threshold. The command also writes a JSON run-metadata file beside the CSV.

## Optional AlignScore scaffold

See [alignscore_scaffold/README.md](alignscore_scaffold/README.md). Its core requirements file is sufficient for the small helper tests, not for installing the full AlignScore package. An authorized compatible checkpoint is required and is not included. Model weights and generated results are excluded by `.gitignore`.

Run commands from inside `alignscore_scaffold/`. The notebook at [00_run_pipeline_colab.ipynb](alignscore_scaffold/notebooks/00_run_pipeline_colab.ipynb) clones this repository and demonstrates the setup path. A synthetic smoke test is not a research evaluation.

If binary metrics are requested from AlignScore, the script selects rows from the explicit development partition (default `dev`). Select the threshold on development data only and freeze it before any held-out evaluation. AlignScore scores are continuous and are not validated four-class predictions.

## Bibliography and paper files

- [IEEE manuscript source](paper/overleaf/main.tex)
- [BibTeX file](paper/overleaf/references.bib)
- [Bibliography/source-paper catalogue](docs/references_catalogue.md)
- [Official full-text paper links and download instructions](papers/README.md)

The catalogue contains five bibliographic entries and links to official full-text records. See [papers/README.md](papers/README.md) for official PDF links and reuse terms. Run [the ACL paper download script](papers/download_open_acl_papers.sh) from the repository root to download the three ACL PDFs into papers/pdfs/. The two DeBERTa PDFs are linked but not mirrored pending confirmation of their paper-specific reuse licenses. The IEEE LaTeX source compiles through GitHub Actions; its PDF is published as the ieee-manuscript-pdf workflow artifact.

## Repository structure

```text
.
├── .github/workflows/     # Python-version matrix CI checks
├── alignscore_scaffold/   # Separate AlignScore helper, tests and Colab notebook
├── data/
│   ├── processed/         # Synthetic examples, JSON schema, annotation template
│   ├── raw/               # Instructions only; no corpus bundled
│   └── source_manifest_template.csv
├── docs/                  # Protocol, labels, references, data management and verification
├── models/                # Instructions only; no model weights
├── paper/overleaf/        # IEEE LaTeX source and BibTeX
├── papers/                # Official PDF links, license notes and ACL download script
├── prompts/               # Research workflow prompt templates
├── reports/               # Report template and experiment status note
├── scripts/               # Root baseline CLI
├── src/citation_drift/    # Root TF-IDF baseline package
├── tests/                 # Root baseline tests
├── CHANGELOG.md
├── CITATION.cff
├── CONTRIBUTING.md
├── LICENSE
├── pytest.ini
└── requirements.txt
```

## Verification status

| Component | Current status |
|---|---|
| Root data loader and TF-IDF baseline | Implemented; automated tests run in GitHub Actions |
| Root CLI | Included in automated smoke test |
| Unavailable-evidence handling | Records are retained but not assigned a similarity score |
| AlignScore helper tests | Run separately in GitHub Actions |
| Official AlignScore installation/checkpoint inference | Not yet verified |
| Real research corpus and annotated dataset | Not included |
| Full text of the five referenced papers | Not included; metadata and links only |
| IEEE manuscript | LaTeX source and BibTeX included; PDF build published as a GitHub Actions artifact |

Do not present synthetic examples as scientific findings. Do not claim AlignScore results until checkpoint-backed inference has been run and outputs have been preserved.

## Reproducibility

For each actual run, retain dataset version and license, model/package versions, model checkpoint provenance and SHA-256, prompts and generation settings, paper-level split IDs, random seed, exact command, raw output and evaluation script. Split by source paper to avoid leakage. Record annotators' independent labels before adjudication.

## Contributing and license

See [CONTRIBUTING.md](CONTRIBUTING.md) for development checks, [research_data_management.md](docs/research_data_management.md) for data-handling and release rules, and [verification_status.md](docs/verification_status.md) for the latest verified commit and test status. [CHANGELOG.md](CHANGELOG.md) records repository-level changes. The current [LICENSE](LICENSE) is an all-rights-reserved notice; this repository is public to view but is not granted an open-source reuse license. Third-party datasets, papers, checkpoints and tools remain subject to their own terms.
