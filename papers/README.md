# Research paper access

This folder indexes the five papers cited in the current IEEE manuscript and records the official PDF URL and reuse conditions.

## Papers included in this repository

| Paper | Repository PDF | Reuse note |
|---|---|---|
| Wadden et al. (2020), *Fact or Fiction: Verifying Scientific Claims* | [papers/pdfs/Wadden_2020_Fact_or_Fiction.pdf](pdfs/Wadden_2020_Fact_or_Fiction.pdf) | CC BY 4.0 (ACL Anthology policy for 2016+) |
| Bowman et al. (2015), *A Large Annotated Corpus for Learning Natural Language Inference* (SNLI) | [papers/pdfs/Bowman_2015_SNLI.pdf](pdfs/Bowman_2015_SNLI.pdf) | CC BY-NC-SA 3.0; ACL permits copies for teaching/research; non-commercial and ShareAlike terms apply |
| Williams et al. (2018), *A Broad-Coverage Challenge Corpus for Sentence Understanding through Inference* (MultiNLI) | [papers/pdfs/Williams_2018_MultiNLI.pdf](pdfs/Williams_2018_MultiNLI.pdf) | CC BY 4.0 (ACL Anthology policy for 2016+) |

All three are unmodified PDFs retrieved from the official ACL Anthology PDF endpoints. See [pdfs/README.md](pdfs/README.md) and [source_manifest.csv](source_manifest.csv) for notices and SHA-256 checksums are tracked separately in the release/verification notes.

## Papers linked but not mirrored

| Paper | Official PDF | Reason |
|---|---|---|
| He et al. (2021), *DeBERTa: Decoding-Enhanced BERT with Disentangled Attention* | https://arxiv.org/pdf/2006.03654 | Individual redistribution license not confirmed |
| He et al. (2023), *DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing* | https://openreview.net/pdf?id=sE7-XhLxHA | Paper-specific redistribution license not confirmed |

The two DeBERTa papers are deliberately linked to their official hosts rather than copied into this repository until their individual reuse rights are confirmed.

## Re-download source copies

From the repository root:

    bash papers/download_open_acl_papers.sh

The script downloads the three ACL Anthology PDFs into `papers/pdfs/`, checks the PDF signature and prints SHA-256 checksums. It does not download or mirror the two DeBERTa PDFs.

## Compiled IEEE manuscript

The compiled conference-style PDF is committed at [paper/overleaf/main.pdf](../paper/overleaf/main.pdf). The GitHub Actions workflow also uploads `ieee-manuscript-pdf` and `acl-source-papers-pdfs` artifacts, retained for 30 days.

## Important

Retain the source-paper attribution and license notices when reusing or sharing these unmodified copies. The repository's root all-rights-reserved notice does not override the separate terms applying to the third-party PDFs.
