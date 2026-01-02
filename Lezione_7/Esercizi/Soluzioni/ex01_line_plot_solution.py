"""EX02 - Bar chart (vendite per mese)

Obiettivo:
1) Crea un bar chart con 12 mesi.
2) Evidenzia il mese massimo con un colore diverso.
3) Aggiungi etichette sopra ogni barra (valore intero).
4) Salva in outputs/ex02_bar_chart.png (dpi=150).

Suggerimento:
- Usa ax.bar(...) e poi un ciclo sulle barre per scrivere le etichette.
"""

import numpy as np
import matplotlib.pyplot as plt


def main():
    rng = np.random.default_rng(42)
    mesi = np.arange(1, 13)
    vendite = rng.integers(80, 170, size=12)

    # 1) fig, ax
    fig, ax = plt.subplots(figsize=(10, 5))

    # 2) Trova il mese con vendite massime
    idx_max = np.argmax(vendite)

    # Colori: tutti blu, tranne il massimo in arancione
    colori = ["steelblue"] * 12
    colori[idx_max] = "orange"

    # 3) Bar chart
    bars = ax.bar(mesi, vendite, color=colori)

    # 4) Etichette sopra ogni barra
    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + 2,
            f"{int(height)}",
            ha="center",
            va="bottom",
            fontsize=9
        )

    # 5) Titolo, assi, griglia
    ax.set_title("Vendite mensili")
    ax.set_xlabel("Mese")
    ax.set_ylabel("Vendite")
    ax.set_xticks(mesi)
    ax.grid(axis="y", alpha=0.3)

    # 6) Export
    fig.savefig("outputs/ex02_bar_chart.png", dpi=150, bbox_inches="tight")

    plt.show()


if __name__ == '__main__':
    main()
