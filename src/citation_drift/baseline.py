"""A lightweight lexical similarity baseline; not an entailment model."""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def score_claims(records):
    pairs = [(r["claim"], r["evidence"]) for r in records]
    if not pairs:
        return []
    corpus = [text for pair in pairs for text in pair]
    matrix = TfidfVectorizer(ngram_range=(1, 2), stop_words="english").fit_transform(corpus)
    return [float(cosine_similarity(matrix[2*i], matrix[2*i+1])[0, 0]) for i in range(len(pairs))]

def add_baseline_fields(records, threshold=0.15):
    scores = score_claims(records)
    output = []
    for record, score in zip(records, scores):
        row = dict(record)
        row["similarity_score"] = score
        row["baseline_flag"] = "REVIEW_HIGH_SIMILARITY" if score >= threshold else "REVIEW_LOW_SIMILARITY"
        row["baseline_note"] = "Similarity heuristic only; not a support classification."
        output.append(row)
    return output
