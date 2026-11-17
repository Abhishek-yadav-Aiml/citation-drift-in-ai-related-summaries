from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def save_score_histogram(scores, output_path):
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    plt.figure(figsize=(7, 4))
    plt.hist(scores, bins=20)
    plt.xlabel("AlignScore")
    plt.ylabel("Number of claim-evidence pairs")
    plt.title("AlignScore score distribution")
    plt.tight_layout()
    plt.savefig(output_path, dpi=160)
    plt.close()
