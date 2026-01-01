"""
Esempi avanzati (dashboard, date, heatmap)
03 - Subplots dashboard
Scopo: creare un layout 2x2 con grafici diversi (line, bar, scatter, hist).
"""

import numpy as np
import matplotlib.pyplot as plt

def main():
    rng = np.random.default_rng(42)

    x = np.arange(1, 13)
    vendite = rng.integers(80, 170, size=12)
    costi = rng.integers(40, 120, size=12)
    margine = vendite - costi

    punti_x = rng.normal(0, 1, 300)
    punti_y = 0.5 * punti_x + rng.normal(0, 1, 300)

    fig, axs = plt.subplots(2, 2, figsize=(10, 6), layout="constrained")

    # (0,0) Line plot
    axs[0, 0].plot(x, vendite, marker="o", label="Vendite")
    axs[0, 0].plot(x, costi, marker="o", label="Costi")
    axs[0, 0].set_title("Trend mensile")
    axs[0, 0].set_xlabel("Mese")
    axs[0, 0].set_ylabel("€")
    axs[0, 0].grid(True, alpha=0.25)
    axs[0, 0].legend()

    # (0,1) Bar chart
    axs[0, 1].bar(x, margine)
    axs[0, 1].axhline(0, color="white", linewidth=1, alpha=0.6)
    axs[0, 1].set_title("Margine (Vendite - Costi)")
    axs[0, 1].set_xlabel("Mese")
    axs[0, 1].set_ylabel("€")

    # (1,0) Scatter
    axs[1, 0].scatter(punti_x, punti_y, s=12, alpha=0.6)
    axs[1, 0].set_title("Scatter: correlazione")
    axs[1, 0].set_xlabel("x")
    axs[1, 0].set_ylabel("y")
    axs[1, 0].grid(True, alpha=0.25)

    # (1,1) Histogram
    dati = rng.normal(100, 15, 1000)
    axs[1, 1].hist(dati, bins=25, alpha=0.85)
    axs[1, 1].set_title("Distribuzione (istogramma)")
    axs[1, 1].set_xlabel("Valore")
    axs[1, 1].set_ylabel("Frequenza")

    fig.suptitle("Mini dashboard Matplotlib", fontsize=14)
    plt.show()

if __name__ == "__main__":
    main()
