from pathlib import Path
from citation_drift.data import load_jsonl
from citation_drift.baseline import add_baseline_fields

DATA = Path(__file__).parents[1] / "data/processed/sample_claim_evidence.jsonl"

def test_sample_loads():
    rows = load_jsonl(DATA)
    assert len(rows) >= 1

def test_baseline_scores_are_bounded():
    rows = add_baseline_fields(load_jsonl(DATA))
    assert all(0.0 <= r["similarity_score"] <= 1.0 for r in rows)
    assert all("not a support classification" in r["baseline_note"] for r in rows)
