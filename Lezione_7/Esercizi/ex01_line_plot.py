"""EX01 - Line plot (2 serie)

Obiettivo:
1) Crea un line plot con 2 serie (es. sin e cos).
2) Aggiungi: titolo, label assi, griglia, legenda.
3) Salva il grafico in outputs/ex01_line_plot.png (dpi=150).

Vincoli:
- Usa la OO API: fig, ax = plt.subplots().
- Non usare plt.plot(...) direttamente.
"""

import numpy as np
import matplotlib.pyplot as plt


def main():
    x = np.linspace(0, 2*np.pi, 200)
    y1 = np.sin(x)
    y2 = np.cos(x)

    # TODO: crea fig, ax
    # fig, ax = ...

    # TODO: disegna 2 linee con label
    # ax.plot(x, y1, ..., label='sin(x)')
    # ax.plot(x, y2, ..., label='cos(x)')

    # TODO: titolo/assi/griglia/legenda

    # TODO: export
    # fig.savefig('outputs/ex01_line_plot.png', dpi=150, bbox_inches='tight')

    plt.show()


if __name__ == '__main__':
    main()
