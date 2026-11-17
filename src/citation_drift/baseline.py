"""A lexical similarity review signal; it is not an entailment model."""
import math

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def score_claims(records):
    """Return one score per record; None means evidence cannot be scored."""
    scores = [None] * len(records)
    eligible_indices = [
        i for i, row in enumerate(records)
        if row.get("evidence_status") == "available"
        and isinstance(row.get("claim"), str) and row["claim"].strip()
        and isinstance(row.get("evidence"), str) and row["evidence"].strip()
    ]
    if not eligible_indices:
        return scores

    corpus = []
    for i in eligible_indices:
        corpus.extend([records[i]["claim"], records[i]["evidence"]])

    vectorizer = TfidfVectorizer(
        ngram_range=(1, 2),
        stop_words="english",
        strip_accents="unicode",
    )
    try:
        matrix = vectorizer.fit_transform(corpus)
    except ValueError as exc:
        # A corpus made only of stop words has no usable TF-IDF vocabulary.
        if "empty vocabulary" not in str(exc).lower():
            raise
        return scores

    for pair_position, record_index in enumerate(eligible_indices):
        claim_vector = matrix[2 * pair_position]
        evidence_vector = matrix[2 * pair_position + 1]
        if claim_vector.nnz == 0 or evidence_vector.nnz == 0:
            continue
        scores[record_index] = float(
            cosine_similarity(claim_vector, evidence_vector)[0, 0]
        )
    return scores


def add_baseline_fields(records, threshold=0.15):
    """Attach review flags without inventing support labels."""
    if not isinstance(threshold, (int, float)) or not math.isfinite(threshold):
        raise ValueError("threshold must be a finite number between 0 and 1")
    if not 0.0 <= threshold <= 1.0:
        raise ValueError("threshold must be between 0 and 1")

    scores = score_claims(records)
    output = []
    for record, score in zip(records, scores):
        row = dict(record)
        row["similarity_score"] = score
        if row.get("evidence_status") != "available" or not row.get("evidence", "").strip():
            row["baseline_flag"] = "NOT_SCORED_EVIDENCE_UNAVAILABLE"
            row["baseline_note"] = (
                "No similarity score: evidence is unavailable, unretrieved, or empty."
            )
        elif score is None:
            row["baseline_flag"] = "NOT_SCORED_NO_USABLE_TOKENS"
            row["baseline_note"] = (
                "No similarity score: claim or evidence produced no usable TF-IDF terms."
            )
        else:
            row["baseline_flag"] = (
                "REVIEW_HIGH_SIMILARITY" if score >= threshold
                else "REVIEW_LOW_SIMILARITY"
            )
            row["baseline_note"] = (
                "Similarity heuristic only; not a factual support classification."
            )
        output.append(row)
    return output
