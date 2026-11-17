import numpy as np
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, confusion_matrix

def evaluate_binary(records, threshold, positive_label="SUPPORTED",
                    negative_labels=("NOT_SUPPORTED_IN_INSPECTED_SOURCE",)):
    y_true, y_pred = [], []
    for row in records:
        label = row.get("gold_label")
        if label == positive_label:
            y_true.append(1)
        elif label in negative_labels:
            y_true.append(0)
        else:
            continue
        y_pred.append(1 if row["alignscore"] >= threshold else 0)
    if not y_true:
        raise ValueError("No records eligible for the declared binary mapping")
    precision, recall, f1, support = precision_recall_fscore_support(
        y_true, y_pred, labels=[0, 1], zero_division=0)
    return {
        "n_evaluated": len(y_true), "threshold": float(threshold),
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "macro_f1": float(np.mean(f1)),
        "per_class": {
            "negative": {"precision": float(precision[0]), "recall": float(recall[0]),
                         "f1": float(f1[0]), "support": int(support[0])},
            "positive": {"precision": float(precision[1]), "recall": float(recall[1]),
                         "f1": float(f1[1]), "support": int(support[1])}},
        "confusion_matrix_labels_0_1": confusion_matrix(y_true, y_pred, labels=[0, 1]).tolist()
    }
