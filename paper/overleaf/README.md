# IEEE / Overleaf manuscript

The manuscript is supplied as:
- `main.tex` — IEEE conference LaTeX source.
- `references.bib` — machine-readable BibTeX entries matching the five cited works.
- `main.pdf` — compiled two-page IEEE conference draft, committed to the repository.

The bibliography is embedded directly in `main.tex` so the draft compiles without a separate BibTeX run. The `references.bib` file is retained as a reusable bibliography source.

## Compile locally

Install a TeX Live distribution with IEEEtran, cite, booktabs, amsmath and hyperref packages, then run from this directory:

    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    pdflatex -interaction=nonstopmode -halt-on-error main.tex

The GitHub Actions workflow compiles the manuscript, downloads the permitted ACL papers, commits the generated PDFs to `main`, and also publishes downloadable artifacts.

## Before submission

Replace the generic author/institution/contact fields in `main.tex`. Review all bibliographic details, the reported metrics, and the two-page layout. The current text is explicitly a preliminary SciFact claim-verification baseline; it is not a completed evaluation of citation drift on AI-generated summaries and it contains no AlignScore results. Do not present it as a final paper until the missing experiment and reproducibility materials are completed.
