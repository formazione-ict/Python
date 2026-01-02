"""EX05 - Heatmap (imshow) + colorbar

Obiettivo:
1) Crea una matrice 8x10 di valori casuali.
2) Visualizza con imshow + colormap.
3) Aggiungi colorbar con label.
4) Salva in outputs/ex05_heatmap.png.
"""

import numpy as np
import matplotlib.pyplot as plt


def main():
    rng = np.random.default_rng(99)
    M = rng.normal(0, 1, size=(8, 10))

    # 1) Figura e asse
    fig, ax = plt.subplots(figsize=(8, 5))

    # 2) Heatmap
    im = ax.imshow(M, aspect='auto', cmap='viridis')

    # 3) Colorbar
    fig.colorbar(im, ax=ax, label='Intensità')

    # 4) Titolo e assi
    ax.set_title("Heatmap 8x10")
    ax.set_xlabel("Colonne")
    ax.set_ylabel("Righe")

    # 5) Export
    fig.savefig("outputs/ex05_heatmap.png", dpi=150, bbox_inches="tight")

    plt.show()


if __name__ == '__main__':
    main()