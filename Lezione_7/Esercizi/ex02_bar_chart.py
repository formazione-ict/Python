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

    # TODO: fig, ax = plt.subplots(...)

    # TODO: trova indice del massimo e definisci i colori

    # TODO: bars = ax.bar(mesi, vendite, color=colori)

    # TODO: ciclo su bars per scrivere le etichette

    # TODO: titolo/assi/griglia

    # TODO: export

    plt.show()


if __name__ == '__main__':
    main()
