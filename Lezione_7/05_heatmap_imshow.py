"""
Esempi avanzati (dashboard, date, heatmap)
05 - Heatmap con imshow
Scopo: visualizzare una matrice (es. correlazioni, intensità, KPI) con colori.
"""

import numpy as np
import matplotlib.pyplot as plt

def main():
    rng = np.random.default_rng(123)
    M = rng.normal(0, 1, size=(10, 12))

    fig, ax = plt.subplots(figsize=(10, 4), layout="constrained")

    im = ax.imshow(M, aspect="auto", cmap="viridis")
    ax.set_title("Heatmap (imshow)")
    ax.set_xlabel("Feature")
    ax.set_ylabel("Osservazioni")

    # Colorbar = legenda dei colori
    fig.colorbar(im, ax=ax, label="Intensità")

    plt.show()

if __name__ == "__main__":
    main()
