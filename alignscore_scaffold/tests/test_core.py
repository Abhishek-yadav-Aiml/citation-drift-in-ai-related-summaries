import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from citation_drift.data import load_jsonl
from citation_drift.preprocess import normalize_whitespace, prepare_records
from citation_drift.retrieval import bm25_top_k

def test_jsonl_and_preprocess(tmp_path):
    p = tmp_path / "x.jsonl"
    p.write_text(json.dumps({
        "example_id":"e1", "source_paper_id":"p1",
        "claim":"A  claim.", "evidence":"Evidence."}) + "\n")
    rows, errors = load_jsonl(p)
    assert not errors
    assert prepare_records(rows)[0]["claim_processed"] == "A claim."

def test_empty_preprocess_rejected():
    try:
        normalize_whitespace("  ")
    except ValueError:
        return
    raise AssertionError("Expected ValueError")

def test_bm25_top_k():
    results = bm25_top_k("transformer encoder", [
        "The proposed system uses a transformer encoder.",
        "We study a supervised learning task."
    ], top_k=1)
    assert len(results) == 1
    assert results[0]["text"] == "The proposed system uses a transformer encoder."
