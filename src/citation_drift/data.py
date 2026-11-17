"""Read and validate claim/evidence JSONL records."""
import json
from pathlib import Path

ALLOWED_STATUSES = {"available", "not_retrieved", "inaccessible", "not_provided"}
ALLOWED_LABELS = {
    "SUPPORTED",
    "PARTIALLY_SUPPORTED",
    "NOT_SUPPORTED_IN_INSPECTED_SOURCE",
    "CONTRADICTED",
    "UNANNOTATED",
}
REQUIRED = {
    "claim_id",
    "summary_id",
    "paper_id",
    "claim",
    "evidence",
    "evidence_status",
}


def load_jsonl(path):
    """Load JSONL and fail with a line-specific message for malformed records."""
    path = Path(path)
    if not path.is_file():
        raise FileNotFoundError(path)

    records = []
    seen_ids = set()
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            item = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"Invalid JSON on line {line_no}: {exc}") from exc

        if not isinstance(item, dict):
            raise ValueError(f"Line {line_no}: each JSONL record must be an object")

        missing = REQUIRED - item.keys()
        if missing:
            raise ValueError(f"Line {line_no} missing fields: {sorted(missing)}")

        for field in REQUIRED - {"evidence"}:
            if not isinstance(item[field], str) or not item[field].strip():
                raise ValueError(f"Line {line_no}: {field} must be a non-empty string")

        if not isinstance(item["evidence"], str):
            raise ValueError(f"Line {line_no}: evidence must be a string")

        status = item["evidence_status"]
        if not isinstance(status, str) or status not in ALLOWED_STATUSES:
            raise ValueError(
                f"Line {line_no}: evidence_status must be one of {sorted(ALLOWED_STATUSES)}"
            )
        if status == "available" and not item["evidence"].strip():
            raise ValueError(
                f"Line {line_no}: evidence cannot be empty when evidence_status is 'available'"
            )

        label = item.get("gold_label", "UNANNOTATED")
        if not isinstance(label, str) or label not in ALLOWED_LABELS:
            raise ValueError(f"Line {line_no}: invalid gold_label {label!r}")

        if item["claim_id"] in seen_ids:
            raise ValueError(f"Line {line_no}: duplicate claim_id {item['claim_id']!r}")
        seen_ids.add(item["claim_id"])
        records.append(item)

    if not records:
        raise ValueError(f"No records found in {path}")
    return records
