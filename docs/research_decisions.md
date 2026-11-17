# Research decision record

## Primary research question
For claims in AI-generated computer-science literature summaries, how does evidence context (abstract-only versus automatically retrieved full-text passages) affect claim-level citation-support evaluation?

## Secondary research question
How much verification error is associated with retrieval failure, comparing BM25-retrieved evidence and human-selected evidence?

## Proposed protocol
- Annotate claim/source pairs with four support labels and a separate evidence-availability label.
- Split data by source paper to prevent leakage.
- Compare abstract-only, BM25-retrieved passage and human-selected evidence contexts.
- Treat lexical similarity and AlignScore as continuous signals, not validated four-class classifiers.
- Any binary threshold is selected on development data and frozen before test.
- A pilot target of 12–20 papers and 60–80 claim-evidence pairs is a feasibility target, not a completed sample.

## Scope cautions
CS-PaperSum is a candidate source-paper pool, not assumed to be a ready-made claim-citation benchmark. Inspect its schema, citation markers, full-text availability and license. Verify dataset, checkpoint and paper licenses before redistribution.
