# Data dictionary

The root TF-IDF baseline consumes one JSON object per line in `data/processed/*.jsonl`. Its expected schema is also provided as [schema.json](../data/processed/schema.json).

| Field | Required | Type | Description |
|---|---:|---|---|
| `claim_id` | yes | string | Unique identifier for one atomic claim–citation unit |
| `summary_id` | yes | string | Identifier for the generated summary |
| `paper_id` | yes | string | Stable identifier for the cited source paper |
| `claim` | yes | string | Atomic factual claim text |
| `evidence` | yes | string | Exact inspected evidence passage; may be empty only when evidence is unavailable |
| `evidence_status` | yes | string | One of the statuses listed below |
| `gold_label` | no | string | Human annotation label; defaults to `UNANNOTATED` |
| `source_location` | no | string | Page, section, paragraph or URL fragment for the evidence |
| `annotator_id` | no | string | Pseudonymous annotator identifier |
| `rationale` | no | string | Short reason for the annotation |

## Evidence availability values

Values are lowercase and must be one of:
- `available`
- `not_retrieved`
- `inaccessible`
- `not_provided`

When `evidence_status` is `available`, `evidence` must contain non-whitespace text. Other statuses may have empty evidence. The root TF-IDF baseline does not score records whose evidence is unavailable.

## Gold support labels

- `SUPPORTED`
- `PARTIALLY_SUPPORTED`
- `NOT_SUPPORTED_IN_INSPECTED_SOURCE`
- `CONTRADICTED`
- `UNANNOTATED`

`UNANNOTATED` is a workflow marker, not a fifth support class. Do not include it in four-class evaluation. Do not convert `not_retrieved`, `inaccessible`, or `not_provided` into `NOT_SUPPORTED_IN_INSPECTED_SOURCE`.

## Relationship and split rules

- Keep each atomic claim's source-paper ID stable across all conditions.
- Assign splits at the paper level, not the individual-claim level, to avoid leakage.
- If one summary claim cites multiple papers, retain separate source-level claim–paper records and preserve a shared group identifier in an optional field.
- Preserve original summary sentence and citation marker in the annotation export when available, even if those are stored in an extended schema.
