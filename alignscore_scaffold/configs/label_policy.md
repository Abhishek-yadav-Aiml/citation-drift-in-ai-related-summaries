# Label and score policy

AlignScore returns a continuous factual-consistency/alignment score. It is not, by itself, a validated four-class classifier.

Human support labels:
- SUPPORTED
- PARTIALLY_SUPPORTED
- NOT_SUPPORTED_IN_INSPECTED_SOURCE
- CONTRADICTED

Evidence availability is separate:
- AVAILABLE
- INSUFFICIENT_ACCESS
- INSUFFICIENT_RETRIEVAL
- INSUFFICIENT_CONTEXT

Do not label inaccessible or unretrieved evidence as unsupported. Use CONTRADICTED only when inspected source material conflicts with the claim.

The optional binary calculation maps SUPPORTED to positive and NOT_SUPPORTED_IN_INSPECTED_SOURCE to negative. Partial and contradicted labels are excluded from that calculation. Select thresholds on development data and freeze before test evaluation.
