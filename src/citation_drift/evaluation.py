"""Metrics for human-annotated labels."""
from sklearn.metrics import classification_report, confusion_matrix

EVALUATED_LABELS = ["SUPPORTED", "PARTIALLY_SUPPORTED", "NOT_SUPPORTED_IN_INSPECTED_SOURCE", "CONTRADICTED"]

def evaluate(gold, predicted):
    if len(gold) != len(predicted):
        raise ValueError("gold and predicted must have equal length")
    return {
        "classification_report": classification_report(gold, predicted, labels=EVALUATED_LABELS, zero_division=0, output_dict=True),
        "confusion_matrix": confusion_matrix(gold, predicted, labels=EVALUATED_LABELS).tolist(),
        "labels": EVALUATED_LABELS,
    }
}