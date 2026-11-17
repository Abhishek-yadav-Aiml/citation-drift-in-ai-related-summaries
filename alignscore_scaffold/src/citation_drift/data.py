import json
from pathlib import Path

REQUIRED = {"example_id", "source_paper_id", "claim", "evidence"}
ALLOWED_LABELS = {"SUPPORTED", "PARTIALLY_SUPPORTED", "NOT_SUPPORTED_IN_INSPECTED_SOURCE", "CONTRADICTED"}

def load_jsonl(path):
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(path)
    records, errors, seen = [], [], set()
    with path.open(encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                errors.append(f"line {line_no}: invalid JSON: {exc}")
                continue
            if not isinstance(row, dict):
                errors.append(f"line {line_no}: expected object")
                continue
            missing = REQUIRED - row.keys()
            if missing:
                errors.append(f"line {line_no}: missing {sorted(missing)}")
                continue
            if not all(isinstance(row[k], str) and row[k].strip() for k in REQUIRED):
                errors.append(f"line {line_no}: required values must be non-empty strings")
                continue
            if row["example_id"] in seen:
                errors.append(f"line {line_no}: duplicate example_id")
                continue
            if row.get("gold_label") is not None and row["gold_label"] not in ALLOWED_LABELS:
                errors.append(f"line {line_no}: invalid gold_label")
                continue
            seen.add(row["example_id"])
            records.append(row)
    if not records:
        raise ValueError(f"No valid records loaded. Errors: {errors[:5]}")
    return records, errors
