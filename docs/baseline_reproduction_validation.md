# Baseline reproduction validation status

## TF-IDF lexical baseline
The repository includes a simple TF-IDF cosine-similarity baseline. Its score is a lexical similarity signal, not factual entailment or truth. Run the supplied tests and sample command before relying on output.

## AlignScore
Status: NOT VALIDATED. The author reported dependency/import problems, including missing spaCy and click modules. No successful end-to-end AlignScore import, checkpoint load, inference, prediction file or reproducible metric output has been confirmed. The AlignScore subproject is a scaffold only.

## Separate SciFact / DeBERTa preliminary experiment
The author separately reported a SciFact development-set experiment with 338 claim-evidence pairs (216 SUPPORT, 122 CONTRADICT), using cross-encoder/nli-deberta-v3-base without fine-tuning. Reported overall accuracy counting NEUTRAL as incorrect: 45.56% (154/338); non-neutral coverage: 50.30% (170/338); conditional accuracy on non-neutral predictions: 90.59%; conditional macro F1: 0.91. These are user-reported figures from a separate Colab run; executable source code and raw outputs for that run are not included.

## Reproduction requirements
Record exact dataset release and license, environment/package versions, model revision, commands, random seeds, split, raw prediction outputs and checkpoint checksum. Re-run from a clean environment and retain logs before describing an experiment as reproduced.
