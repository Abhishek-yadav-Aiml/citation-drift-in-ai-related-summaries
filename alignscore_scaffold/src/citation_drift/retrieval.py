import re
from rank_bm25 import BM25Okapi

def tokenize(text):
    return re.findall(r"\w+", text.lower())

def bm25_top_k(claim, passages, top_k=5):
    if not passages or top_k <= 0:
        return []
    corpus = [tokenize(p) for p in passages]
    if not any(corpus):
        return []
    model = BM25Okapi(corpus)
    scores = model.get_scores(tokenize(claim))
    order = sorted(range(len(passages)), key=lambda i: scores[i], reverse=True)
    return [{"passage_id": f"p{i}", "rank": rank + 1,
             "bm25_score": float(scores[i]), "text": passages[i]}
            for rank, i in enumerate(order[:top_k])]
