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

    # TODO: fig, ax = plt.subplots(...)

    # TODO: im = ax.imshow(M, aspect='auto', cmap='viridis')

    # TODO: fig.colorbar(im, ax=ax, label='Intensità')

    # TODO: titolo/assi

    # TODO: export

    plt.show()


if __name__ == '__main__':
    main()
