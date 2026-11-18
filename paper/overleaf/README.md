# IEEE / Overleaf manuscript

The manuscript is supplied as:
- main.tex — IEEE conference LaTeX source.
- references.bib — machine-readable BibTeX entries matching the five cited works.
- The bibliography is embedded directly in main.tex so the draft compiles in environments without a separate BibTeX installation.

## Compile locally

Install a TeX Live distribution with IEEEtran, cite, booktabs, amsmath and hyperref packages, then run from this directory:

    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    pdflatex -interaction=nonstopmode -halt-on-error main.tex

The second run resolves citation and table references. The GitHub Actions workflow also compiles the manuscript and publishes an artifact named ieee-manuscript-pdf for 30 days.

## Before submission

Replace the generic author/institution/contact fields in main.tex. Review all bibliographic details, the reported metrics, and the two-page layout. The current text is explicitly a preliminary SciFact claim-verification baseline; it is not a completed evaluation of citation drift on AI-generated summaries and it contains no AlignScore results. Do not present it as a final paper until the missing experiment and reproducibility materials are completed.
