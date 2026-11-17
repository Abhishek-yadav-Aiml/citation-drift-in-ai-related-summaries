# Data dictionary

| Field | Required | Description |
|---|---:|---|
| claim_id | yes | Unique atomic-claim identifier |
| summary_id | yes | Generated-summary identifier |
| paper_id | yes | Stable cited-paper identifier |
| claim | yes | Atomic factual claim |
| evidence | yes | Exact inspected passage, or empty if unavailable |
| evidence_status | yes | available / not_retrieved / inaccessible / not_provided |
| gold_label | no | Human annotation label |
| source_location | no | Page, section, paragraph or URL fragment |
| annotator_id | no | Annotator pseudonym |
| rationale | no | Short reason for label |
