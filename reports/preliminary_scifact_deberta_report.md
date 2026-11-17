# Preliminary experiment: SciFact + DeBERTa NLI baseline

## Status and separation
This is a separately reported preliminary Colab experiment. It is not produced by the repository's TF-IDF baseline or the AlignScore scaffold. The experiment source notebook/script and raw prediction file were not present among the files available for this repository upload.

## Setup reported by the author
- Dataset: SciFact development split
- Claim-evidence pairs: 338
- Gold labels: 216 SUPPORT and 122 CONTRADICT
- Model: cross-encoder/nli-deberta-v3-base
- No fine-tuning
- Model class indices: 0 contradiction, 1 entailment, 2 neutral
- Comparison mapping: entailment to SUPPORT; contradiction to CONTRADICT; neutral retained as NEUTRAL

## Reported results
| Measure | Value |
|---|---:|
| Overall accuracy across 338, with NEUTRAL counted incorrect | 45.56% (154/338) |
| Non-neutral predictions | 170 |
| Coverage | 50.30% |
| Correct non-neutral predictions | 154 |
| Conditional accuracy on non-neutral predictions | 90.59% |
| Conditional macro F1 | 0.91 |
| NEUTRAL predictions | 168 |

Confusion matrix (gold rows, predicted columns):

| Gold / predicted | SUPPORT | CONTRADICT | NEUTRAL |
|---|---:|---:|---:|
| SUPPORT | 73 | 13 | 130 |
| CONTRADICT | 3 | 81 | 38 |

## Interpretation caveats
These are author-reported metrics, not independently reproduced in this repository. Neutral coverage and conditional accuracy describe selective predictions; do not present conditional accuracy as overall accuracy. Record the exact SciFact release, license, runtime, model revision, code and raw outputs before claiming reproducibility.
