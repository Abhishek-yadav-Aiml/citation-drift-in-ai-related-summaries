"""Read and validate claim/evidence JSONL records."""
import json
from pathlib import Path

ALLOWED_STATUSES = {"available", "not_retrieved", "inaccessible", "not_provided"}
ALLOWED_LABELS = {"SUPPORTED", "PARTIALLY_SUPPORTED", "NOT_SUPPORTED_IN_INSPECTED_SOURCE", "CONTRADICTED", "UNANNOTATED"}
REQUIRED = {"claim_id", "summary_id", "paper_id", "claim", "evidence", "evidence_status"}

def load_jsonl(path):
    records = []
    for line_no, line in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            item = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"Invalid JSON on line {line_no}: {exc}") from exc
        missing = REQUIRED - item.keys()
        if missing:
            raise ValueError(f"Line {line_no} missing fields: {sorted(missing)}")
        if item["evidence_status"] not in ALLOWED_STATUSES:
            raise ValueError(f"Line {line_no}: invalid evidence_status")
        label = item.get("gold_label", "UNANNOTATED")
        if label not in ALLOWED_LABELS:
            raise ValueError(f"Line {line_no}: invalid gold_label {label!r}")
        records.append(item)
    return records
