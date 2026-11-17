import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from citation_drift.data import load_jsonl
from citation_drift.preprocess import normalize_whitespace, prepare_records
from citation_drift.retrieval import bm25_top_k
from citation_drift.evaluate import evaluate_binary


def test_jsonl_and_preprocess(tmp_path):
    p = tmp_path / "x.jsonl"
    p.write_text(json.dumps({
        "example_id": "e1",
        "source_paper_id": "p1",
        "claim": "A  claim.",
        "evidence": "Evidence."
    }) + "\n", encoding="utf-8")
    rows, errors = load_jsonl(p)
    assert not errors
    assert prepare_records(rows)[0]["claim_processed"] == "A claim."


def test_empty_preprocess_rejected():
    with pytest.raises(ValueError, match="empty"):
        normalize_whitespace("  ")


def test_bm25_top_k():
    results = bm25_top_k("transformer encoder", [
        "The proposed system uses a transformer encoder.",
        "We study a supervised learning task."
    ], top_k=1)
    assert len(results) == 1
    assert results[0]["text"] == "The proposed system uses a transformer encoder."


def test_binary_evaluation_uses_only_declared_labels():
    rows = [
        {"gold_label": "SUPPORTED", "alignscore": 0.9},
        {"gold_label": "NOT_SUPPORTED_IN_INSPECTED_SOURCE", "alignscore": 0.1},
        {"gold_label": "PARTIALLY_SUPPORTED", "alignscore": 0.95},
        {"gold_label": "CONTRADICTED", "alignscore": 0.01},
        {"gold_label": "UNANNOTATED", "alignscore": 0.5},
    ]
    result = evaluate_binary(rows, threshold=0.5)
    assert result["n_evaluated"] == 2
    assert result["accuracy"] == 1.0
    assert result["confusion_matrix_labels_0_1"] == [[1, 0], [0, 1]]


def test_binary_evaluation_rejects_empty_eligible_subset():
    with pytest.raises(ValueError, match="No records eligible"):
        evaluate_binary([
            {"gold_label": "PARTIALLY_SUPPORTED", "alignscore": 0.8}
        ], threshold=0.5)


def test_binary_evaluation_rejects_non_finite_scores():
    with pytest.raises(ValueError, match="non-finite"):
        evaluate_binary([
            {"gold_label": "SUPPORTED", "alignscore": float("nan")}
        ], threshold=0.5)
