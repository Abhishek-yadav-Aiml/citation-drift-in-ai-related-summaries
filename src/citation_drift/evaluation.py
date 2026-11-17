"""Metrics for comparisons against human-annotated support labels."""
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

EVALUATED_LABELS = [
    "SUPPORTED",
    "PARTIALLY_SUPPORTED",
    "NOT_SUPPORTED_IN_INSPECTED_SOURCE",
    "CONTRADICTED",
]


def evaluate(gold, predicted):
    """Evaluate four-way labels; unannotated/unknown labels are rejected."""
    if len(gold) != len(predicted):
        raise ValueError("gold and predicted must have equal length")
    if not gold:
        raise ValueError("at least one labelled example is required")

    valid = set(EVALUATED_LABELS)
    invalid_gold = set(gold) - valid
    invalid_predicted = set(predicted) - valid
    if invalid_gold:
        raise ValueError(f"gold contains labels outside the four-class scheme: {sorted(invalid_gold)}")
    if invalid_predicted:
        raise ValueError(
            f"predicted contains labels outside the four-class scheme: {sorted(invalid_predicted)}"
        )

    report = classification_report(
        gold,
        predicted,
        labels=EVALUATED_LABELS,
        target_names=EVALUATED_LABELS,
        zero_division=0,
        output_dict=True,
    )
    return {
        "n_evaluated": len(gold),
        "accuracy": float(accuracy_score(gold, predicted)),
        "macro_f1": float(report["macro avg"]["f1-score"]),
        "classification_report": report,
        "confusion_matrix": confusion_matrix(
            gold, predicted, labels=EVALUATED_LABELS
        ).tolist(),
        "labels": EVALUATED_LABELS,
    }
