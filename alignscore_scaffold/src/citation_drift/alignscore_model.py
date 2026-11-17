from pathlib import Path

class AlignScoreScorer:
    """Thin adapter around the official AlignScore API."""
    def __init__(self, checkpoint, device="cpu", batch_size=1,
                 model="roberta-base", evaluation_mode="nli_sp"):
        checkpoint = Path(checkpoint)
        if not checkpoint.is_file():
            raise FileNotFoundError(f"AlignScore checkpoint not found: {checkpoint}")
        from alignscore import AlignScore
        self.scorer = AlignScore(model=model, batch_size=batch_size,
                                 device=device, ckpt_path=str(checkpoint),
                                 evaluation_mode=evaluation_mode)

    def score(self, contexts, claims):
        if len(contexts) != len(claims):
            raise ValueError("contexts and claims must have equal length")
        if not contexts:
            return []
        values = self.scorer.score(contexts=contexts, claims=claims)
        scores = [float(x) for x in values]
        if len(scores) != len(claims):
            raise RuntimeError("AlignScore returned an unexpected score count")
        return scores
