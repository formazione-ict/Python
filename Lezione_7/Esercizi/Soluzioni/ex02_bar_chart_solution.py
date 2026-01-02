"""EX03 - Subplots 2x2 (mini dashboard)

Obiettivo:
1) Crea un layout 2x2 con plt.subplots(2, 2, ...).
2) Inserisci:
   - (0,0) line plot
   - (0,1) bar chart
   - (1,0) scatter
   - (1,1) histogram
3) Salva in outputs/ex03_subplots_2x2.png.

Vincoli:
- Usa axs[r, c] e metodi OO.
"""

import numpy as np
import matplotlib.pyplot as plt


def main():
    rng = np.random.default_rng(7)

    x = np.arange(1, 13)
    serie = rng.integers(50, 150, size=12)

    px = rng.normal(0, 1, 300)
    py = 0.7 * px + rng.normal(0, 1, 300)

    dati = rng.normal(100, 15, 1000)

    # 1) Layout 2x2
    fig, axs = plt.subplots(2, 2, figsize=(10, 8), layout='constrained')

    # 2a) Line plot (0,0)
    axs[0, 0].plot(x, serie, marker='o', color='steelblue')
    axs[0, 0].set_title("Line plot")
    axs[0, 0].set_xlabel("Mese")
    axs[0, 0].set_ylabel("Valore")
    axs[0, 0].grid(True, alpha=0.3)

    # 2b) Bar chart (0,1)
    axs[0, 1].bar(x, serie, color='orange')
    axs[0, 1].set_title("Bar chart")
    axs[0, 1].set_xlabel("Mese")
    axs[0, 1].set_ylabel("Valore")
    axs[0, 1].grid(axis='y', alpha=0.3)

    # 2c) Scatter (1,0)
    axs[1, 0].scatter(px, py, alpha=0.6, color='green')
    axs[1, 0].set_title("Scatter")
    axs[1, 0].set_xlabel("px")
    axs[1, 0].set_ylabel("py")
    axs[1, 0].grid(True, alpha=0.3)

    # 2d) Histogram (1,1)
    axs[1, 1].hist(dati, bins=30, color='purple', alpha=0.7)
    axs[1, 1].set_title("Histogram")
    axs[1, 1].set_xlabel("Valore")
    axs[1, 1].set_ylabel("Frequenza")
    axs[1, 1].grid(True, alpha=0.3)

    # 3) Titolo generale
    fig.suptitle("Mini Dashboard 2x2", fontsize=16)

    # 4) Export
    fig.savefig("outputs/ex03_subplots_2x2.png", dpi=150, bbox_inches="tight")

    plt.show()


if __name__ == '__main__':
    main()
