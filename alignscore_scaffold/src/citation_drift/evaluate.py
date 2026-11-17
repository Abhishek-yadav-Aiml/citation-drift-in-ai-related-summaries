import math

import numpy as np
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, confusion_matrix


def evaluate_binary(
    records,
    threshold,
    positive_label="SUPPORTED",
    negative_labels=("NOT_SUPPORTED_IN_INSPECTED_SOURCE",),
):
    """Evaluate only the explicitly declared binary subset.

    Partial, contradicted and unannotated records are excluded rather than
    silently mapped to either class.
    """
    if not isinstance(threshold, (int, float)) or not math.isfinite(threshold):
        raise ValueError("threshold must be a finite number")
    negative_labels = tuple(negative_labels)
    if positive_label in negative_labels:
        raise ValueError("positive_label cannot also appear in negative_labels")

    y_true, y_pred = [], []
    for index, row in enumerate(records):
        label = row.get("gold_label")
        if label == positive_label:
            target = 1
        elif label in negative_labels:
            target = 0
        else:
            continue

        if "alignscore" not in row:
            raise ValueError(f"record {index} has no alignscore")
        score = float(row["alignscore"])
        if not math.isfinite(score):
            raise ValueError(f"record {index} has a non-finite alignscore")

        y_true.append(target)
        y_pred.append(1 if score >= threshold else 0)

    if not y_true:
        raise ValueError("No records eligible for the declared binary mapping")

    precision, recall, f1, support = precision_recall_fscore_support(
        y_true, y_pred, labels=[0, 1], zero_division=0
    )
    return {
        "n_evaluated": len(y_true),
        "threshold": float(threshold),
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "macro_f1": float(np.mean(f1)),
        "per_class": {
            "negative": {
                "precision": float(precision[0]),
                "recall": float(recall[0]),
                "f1": float(f1[0]),
                "support": int(support[0]),
            },
            "positive": {
                "precision": float(precision[1]),
                "recall": float(recall[1]),
                "f1": float(f1[1]),
                "support": int(support[1]),
            },
        },
        "confusion_matrix_labels_0_1": confusion_matrix(
            y_true, y_pred, labels=[0, 1]
        ).tolist(),
    }
