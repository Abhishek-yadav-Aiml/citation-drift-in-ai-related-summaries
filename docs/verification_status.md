# Repository verification status

**Audited branch:** `main`  
**Latest successful GitHub Actions run:** [#32](https://github.com/Abhishek-yadav-Aiml/citation-drift-in-ai-related-summaries/actions/runs/44169690900)  
**Verified commit:** `f62a836c44c5b1174c38158e232f463530161ec6`

The two commits after the verified commit changed only `.gitignore` and the README repository tree. No executable source code, test files, input data, schemas or workflow definitions changed after run #32.

## Automated verification

All six GitHub Actions matrix jobs completed successfully.

| Workflow check | Python versions | Outcome |
|---|---|---|
| Root TF-IDF baseline tests | 3.10, 3.11, 3.12 | PASS |
| Root baseline CLI smoke test | 3.10, 3.11, 3.12 | PASS |
| AlignScore scaffold helper tests | 3.10, 3.11, 3.12 | PASS |

Observed test counts:
- Root test suite: 13 passed.
- AlignScore scaffold helper suite: 6 passed.
- Root sample CLI: wrote 5 synthetic sample records to the temporary CSV output.

## What this verification does not establish

- It does not verify installation of the full external AlignScore package.
- It does not verify compatibility or loading of an AlignScore model checkpoint.
- It does not run AlignScore inference.
- It does not validate real research data, annotation quality, scientific conclusions or a final paper.
- Passing synthetic-example tests does not establish research validity.

## Current repository assets

The branch contains a root TF-IDF baseline, a separate AlignScore scaffold, synthetic JSONL examples, two schema files, annotation/source-manifest templates, research and data-management documentation, an IEEE LaTeX draft and its BibTeX bibliography. The source-paper catalogue is metadata and links only; no full-text source-paper PDFs are included.

## Remaining research validation

1. Add permitted real claim/evidence records with traceable source IDs and dataset provenance.
2. Complete independent human annotation and adjudication.
3. Install and run the external AlignScore baseline with a verified checkpoint.
4. Retain raw predictions, run metadata, error analysis and paper-level split manifests.
5. Compile and review the LaTeX manuscript after the final verified experiment.
