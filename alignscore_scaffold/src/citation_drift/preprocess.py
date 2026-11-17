import re

def normalize_whitespace(text):
    if not isinstance(text, str):
        raise TypeError("text must be str")
    if not text.strip():
        raise ValueError("text cannot be empty")
    return re.sub(r"\\s+", " ", text).strip()

def prepare_records(records):
    output = []
    for row in records:
        item = dict(row)
        item["claim_processed"] = normalize_whitespace(row["claim"])
        item["evidence_processed"] = normalize_whitespace(row["evidence"])
        output.append(item)
    return output
