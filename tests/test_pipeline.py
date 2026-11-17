import json
from pathlib import Path

import pytest

from citation_drift.data import load_jsonl
from citation_drift.baseline import add_baseline_fields, score_claims
from citation_drift.evaluation import evaluate

DATA = Path(__file__).parents[1] / "data/processed/sample_claim_evidence.jsonl"


def test_sample_loads():
    rows = load_jsonl(DATA)
    assert len(rows) == 5


def test_available_evidence_gets_bounded_score():
    rows = add_baseline_fields(load_jsonl(DATA))
    scored = [row for row in rows if row["similarity_score"] is not None]
    assert len(scored) == 4
    assert all(0.0 <= row["similarity_score"] <= 1.0 for row in scored)
    assert all("not a factual support classification" in row["baseline_note"]
               for row in scored)


def test_inaccessible_evidence_is_not_scored():
    rows = add_baseline_fields(load_jsonl(DATA))
    inaccessible = next(row for row in rows if row["evidence_status"] == "inaccessible")
    assert inaccessible["similarity_score"] is None
    assert inaccessible["baseline_flag"] == "NOT_SCORED_EVIDENCE_UNAVAILABLE"


def test_stopword_only_pair_is_not_scored():
    rows = [{
        "claim": "the and or",
        "evidence": "a the and",
        "evidence_status": "available",
    }]
    assert score_claims(rows) == [None]
    assert add_baseline_fields(rows)[0]["baseline_flag"] == "NOT_SCORED_NO_USABLE_TOKENS"


@pytest.mark.parametrize("threshold", [-0.1, 1.1, float("nan"), float("inf")])
def test_invalid_threshold_rejected(threshold):
    with pytest.raises(ValueError):
        add_baseline_fields(load_jsonl(DATA), threshold=threshold)


def test_loader_rejects_empty_available_evidence(tmp_path):
    row = {
        "claim_id": "c1",
        "summary_id": "s1",
        "paper_id": "p1",
        "claim": "A factual statement",
        "evidence": "",
        "evidence_status": "available",
    }
    path = tmp_path / "bad.jsonl"
    path.write_text(json.dumps(row), encoding="utf-8")
    with pytest.raises(ValueError, match="evidence cannot be empty"):
        load_jsonl(path)


def test_loader_allows_empty_inaccessible_evidence(tmp_path):
    row = {
        "claim_id": "c1",
        "summary_id": "s1",
        "paper_id": "p1",
        "claim": "A factual statement",
        "evidence": "",
        "evidence_status": "inaccessible",
        "gold_label": "UNANNOTATED",
    }
    path = tmp_path / "inaccessible.jsonl"
    path.write_text(json.dumps(row), encoding="utf-8")
    loaded = load_jsonl(path)
    assert len(loaded) == 1


def test_four_class_evaluation():
    labels = ["SUPPORTED", "CONTRADICTED", "PARTIALLY_SUPPORTED"]
    result = evaluate(labels, labels)
    assert result["accuracy"] == 1.0
    # The fixed four-class metric includes CONTRADICTED, which has zero support here.
    assert result["macro_f1"] == 0.75


def test_evaluation_rejects_unannotated():
    with pytest.raises(ValueError, match="gold contains labels"):
        evaluate(["UNANNOTATED"], ["SUPPORTED"])
