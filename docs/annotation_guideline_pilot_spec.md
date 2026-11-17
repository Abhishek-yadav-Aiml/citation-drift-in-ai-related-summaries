# Annotation Guideline and Pilot Dataset Specification

**Project:** Detecting Citation Drift in AI-Generated Literature Summaries  
**Version:** 0.1 — draft for pilot  
**Domain:** Computer Science  
**Annotators:** Two independent annotators  

> This is a proposed protocol, not a validated annotation scheme. Calibrate on a small set, revise and version the guide before the main annotation round.

## 1. Objective and unit
For each factual claim in an AI-generated scientific literature summary, judge whether its cited publication supports the claim. The unit is one claim–citation relationship. Preserve the original sentence and context. Split multiple independently verifiable propositions into atomic claims. For a multi-cited claim, create one source-level record per citation and optionally a group-level assessment of the cited set.

## 2. Evidence availability (separate dimension)
- `AVAILABLE`: cited source identified and sufficient text inspected.
- `INSUFFICIENT_ACCESS`: source or relevant full text cannot be accessed.
- `INSUFFICIENT_RETRIEVAL`: source is accessible but retrieval/extraction did not locate adequate passages.
- `INSUFFICIENT_CONTEXT`: claim or source context is too ambiguous to decide.

Do not assign unsupported or contradicted when availability is insufficient.

## 3. Support labels
Assign only when evidence availability is AVAILABLE.
- `SUPPORTED`: inspected source clearly supports all material parts at the stated specificity.
- `PARTIALLY_SUPPORTED`: at least one material part is supported but another part, qualifier, scope, number or relation is not.
- `NOT_SUPPORTED_IN_INSPECTED_SOURCE`: inspected source does not provide adequate support. This is source-relative and does not prove the claim false.
- `CONTRADICTED`: inspected source directly conflicts with a material part. Mere omission is not contradiction.

Topical relevance is not support. A valid DOI is not support. Do not use outside knowledge to fill gaps.

## 4. Abstract-only and full-text passes
Pass A: provide claim, citation metadata and abstract. Record the abstract-only label (or insufficient abstract) and exact abstract span.
Pass B: provide full text or relevant accessible sections. Make a fresh decision, record full-text label, exact evidence and page/section/paragraph. Record whether the decision changed. Do not claim comprehensive full-text review if only selected sections were inspected. The principal label should use full text when adequate full text is available; abstract-only is a separate condition.

## 5. Multi-citation claims
Annotate each claim–paper pair separately. Add a collective cited-set assessment only when the claim plausibly relies on sources jointly. Record which source supports which component. Treat multi-source cases as a separate pilot subset if consistency is uncertain.

## 6. Recommended annotation fields
`sample_id, summary_id, source_paper_id, source_title, source_doi, source_url, source_version_or_access_date, summary_model, summary_model_version, generation_prompt_id, generation_parameters, original_sentence, claim_id, atomic_claim, claim_span_start, claim_span_end, citation_marker, cited_paper_id, abstract_text, abstract_evidence_span, abstract_support_label, fulltext_access_status, fulltext_inspected_scope, fulltext_evidence_span, evidence_page, evidence_section, evidence_availability, fulltext_support_label, multi_source_group_id, annotator_id, annotation_notes, adjudication_label, adjudication_notes, annotation_guide_version`.

Avoid redistributing copyrighted full text unless terms permit it.

## 7. Inclusion and exclusion
Include CS papers with stable metadata, accessible abstracts/full text where possible, AI-generated summaries with traceable citations, and verifiable propositions. Exclude or separately flag unresolved references, uncited claims (unless used as a control), vague opinions, corrupted text, duplicates and inaccessible sources. Keep an access-failure log rather than labeling inaccessible sources unsupported.

## 8. Pilot plan
Initial workload target: 20–30 CS papers and 50–100 claim–citation pairs. This is a planning target, not a power calculation or completed sample. Sample across subareas if feasible, avoid selecting only easy or apparently supported claims, record sampling, and keep paper groups intact across splits.

## 9. Two-annotator workflow
1. Independently label 5–10 calibration examples.
2. Discuss disagreements and revise unclear instructions.
3. Freeze annotation guide v1.0 and record changes.
4. Independently annotate pilot records without seeing the other annotator's labels.
5. Report raw agreement and a chance-corrected statistic (e.g. Cohen's kappa), with class prevalence.
6. Preserve original labels, then adjudicate and record rationale.
7. Version the guide and re-annotate affected records after material changes.

Never overwrite the original independent labels with adjudicated labels.

## 10. Quality checks
Verify original sentences and citation markers, stable source IDs, exact evidence spans and locations, label/availability consistency, explicit contradiction evidence, scope inspected for unsupported labels, partial-claim rationale, duplicate control and paper-level split integrity.

## 11. Stop/go criteria
Pause if annotators confuse unsupported with contradicted, retrieval failure is marked unsupported, claim segmentation changes meaning, access is systematically unavailable, or paper leakage cannot be controlled. Report actual agreement, prevalence, disagreements and adjudication; no single arbitrary agreement threshold proves validity.

## 12. Open decisions and next steps
Still to decide: source corpus/license, single-paper vs multi-paper summaries, exact generation model/prompt, inclusion of collective multi-source support, final sample/split, evidence-span scoring rule, and test-set size. Next: verify corpus rights, calibrate 5–10 examples, revise/freeze the guide, freeze sampling manifest and CSV schema, then begin pilot annotation.
