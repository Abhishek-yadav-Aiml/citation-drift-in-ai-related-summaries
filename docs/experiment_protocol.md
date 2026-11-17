# Experiment protocol

1. Define research question, inclusion criteria and a permitted corpus.
2. Record corpus version, license, access date and paper identifiers.
3. Generate summaries with fixed prompts/model/settings; preserve raw generations.
4. Segment summaries into atomic factual claims.
5. Map each claim to its cited paper and inspect source passages.
6. Annotate support independently; adjudicate disagreements.
7. Compare abstract-only, retrieved-passage and full-text evidence where permitted.
8. Split by paper (not claim) to avoid leakage; tune thresholds on development data only.
9. Report class-wise precision/recall/F1, macro-F1, confusion matrix, coverage, agreement and uncertainty.
10. Preserve prompts, outputs, versions, seeds, split IDs, logs and annotation decisions.

A lexical similarity score is not entailment. NLI predictions are not ground truth. Report inaccessible evidence separately. Never present synthetic smoke-test results as research findings.
