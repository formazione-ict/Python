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

    # TODO: fig, axs = plt.subplots(2, 2, figsize=(...), layout='constrained')

    # TODO: riempi i 4 grafici usando axs[0,0], axs[0,1], ...

    # TODO: fig.suptitle(...)

    # TODO: export

    plt.show()


if __name__ == '__main__':
    main()
