# Research prompts and reproducibility record

For every run, preserve exact prompt text, model/provider/version, date, temperature, token limit, source list and raw output. Do not treat model-generated references as verified.

## Prompt A — literature-summary generation

You are assisting with a scientific literature review in computer science.

Topic: [INSERT TOPIC]

Use only the source papers and metadata supplied below. Do not invent papers, authors, years, DOIs, URLs, results, methods, or datasets. If the supplied source material does not support a statement, omit it or explicitly flag uncertainty. Produce a concise synthesis with claims traceable to supplied source IDs such as [P1]. Keep material limitations and qualifiers.

SOURCE PAPERS:
[INSERT SOURCE IDs, TITLES, ABSTRACTS OR PERMITTED EXTRACTED PASSAGES]

## Prompt B — claim/citation pair extraction

Extract claim-citation pairs from the summary. Preserve original sentence text and citation marker. Split multiple independently verifiable propositions into atomic claims while retaining the original sentence/group ID. For multiple citations, create one pair per cited source. Do not invent markers, titles or source IDs. Return JSON fields: summary_id, claim_id, original_sentence, atomic_claim, citation_marker, source_paper_id.

SUMMARY:
[INSERT SUMMARY]

CITATION MAP:
[INSERT EXACT MARKER-TO-SOURCE MAP]

## Prompt C — atomic-fact decomposition

Split the claim into independently verifiable propositions. Preserve entities, numbers, units, dates, comparison direction, negation, uncertainty and scope qualifiers. Do not add information or strengthen/weaken the claim. Return the original claim and list of atomic facts.

CLAIM:
[INSERT CLAIM]

This is a FActScore-inspired adaptation, not a faithful reproduction of the original FActScore pipeline.

## Prompt D — annotation form

For each claim-source pair, annotators record:
- Support label: SUPPORTED / PARTIALLY_SUPPORTED / NOT_SUPPORTED_IN_INSPECTED_SOURCE / CONTRADICTED
- Evidence availability: AVAILABLE / INSUFFICIENT_ACCESS / INSUFFICIENT_RETRIEVAL / INSUFFICIENT_CONTEXT
- Exact evidence passage and page/section
- Source version and access date
- Rationale

Do not treat inaccessible or unretrieved evidence as unsupported. Use CONTRADICTED only when inspected source material conflicts with the claim.
