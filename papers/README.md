# Research paper access

This folder indexes the five papers cited in the current IEEE manuscript. It gives official publisher/proceedings or author-hosted PDF links and records reuse restrictions.

## Official PDF links

| Paper | Official PDF | Repository handling |
|---|---|---|
| Wadden et al. (2020), *Fact or Fiction: Verifying Scientific Claims* | https://aclanthology.org/2020.emnlp-main.609.pdf | CC BY 4.0; download script provided |
| Bowman et al. (2015), *A Large Annotated Corpus for Learning Natural Language Inference* (SNLI) | https://aclanthology.org/D15-1075.pdf | CC BY-NC-SA 3.0; non-commercial teaching/research copies permitted by ACL notice |
| Williams et al. (2018), *A Broad-Coverage Challenge Corpus for Sentence Understanding through Inference* (MultiNLI) | https://aclanthology.org/N18-1101.pdf | CC BY 4.0; download script provided |
| He et al. (2021), *DeBERTa: Decoding-Enhanced BERT with Disentangled Attention* | https://arxiv.org/pdf/2006.03654 and https://www.microsoft.com/en-us/research/project/deberta/publications/ | Official full-text link only; individual redistribution license not confirmed |
| He et al. (2023), *DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing* | https://openreview.net/pdf?id=sE7-XhLxHA | Official full-text link only; check paper-specific license |

## Download the three ACL papers

From the repository root, run:

    bash papers/download_open_acl_papers.sh

The script downloads the three ACL Anthology PDFs into papers/pdfs/, verifies that each file starts with a PDF signature, and prints SHA-256 checksums. Keep original attribution and license notices alongside unmodified copies.

The automated GitHub workflow builds the IEEE manuscript PDF and publishes it as a downloadable artifact named ieee-manuscript-pdf. Open the Actions run and select Artifacts. A compiled copy is also linked in the task response.

## Important

The ACL download script must be run in an environment with internet access before those PDF binaries exist in the working tree. The DeBERTa papers are deliberately linked rather than mirrored until their individual reuse permissions are confirmed.
