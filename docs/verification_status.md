# Repository verification status

**Audited branch:** `main`  
**Latest asset-publishing workflow:** [#40](https://github.com/Abhishek-yadav-Aiml/citation-drift-in-ai-related-summaries/actions/runs/44222960851)  
**Asset commit:** `089af2955bed57f9ad66a55205a9f0a5f0405b7b`

## Automated verification

Workflow #40 completed successfully. All jobs passed:
- Root TF-IDF test suite and sample CLI on Python 3.10, 3.11 and 3.12.
- AlignScore scaffold helper tests on Python 3.10, 3.11 and 3.12.
- IEEE LaTeX compilation and PDF publication.
- Download of three ACL Anthology source-paper PDFs and repository publication.

Earlier successful test logs show 13 root tests and 6 AlignScore scaffold helper tests. The root CLI smoke test writes five synthetic examples. These are software checks only.

## PDFs now committed to main

- `paper/overleaf/main.pdf` — compiled two-page IEEE conference draft.
- `papers/pdfs/Wadden_2020_Fact_or_Fiction.pdf` — source paper, CC BY 4.0.
- `papers/pdfs/Bowman_2015_SNLI.pdf` — source paper, CC BY-NC-SA 3.0, non-commercial teaching/research and ShareAlike conditions.
- `papers/pdfs/Williams_2018_MultiNLI.pdf` — source paper, CC BY 4.0.

The DeBERTa (2021) and DeBERTaV3 (2023) full texts remain official links only because the paper-specific redistribution permissions were not established in the source review.

## What this verification does not establish

- It does not verify installation of the full external AlignScore package.
- It does not verify compatibility or loading of an AlignScore model checkpoint.
- It does not run AlignScore inference.
- It does not validate real research data, annotation quality, scientific conclusions or a final paper.
- Passing synthetic-example tests does not establish research validity.

## Remaining research validation

1. Add permitted real claim/evidence records with traceable source IDs and dataset provenance.
2. Complete independent human annotation and adjudication.
3. Install and run the external AlignScore baseline with a verified checkpoint.
4. Retain raw predictions, run metadata, error analysis and paper-level split manifests.
5. Replace generic author details in the IEEE draft and review the manuscript after the final verified experiment.
