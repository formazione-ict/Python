"""EX06 - Export (PNG + PDF)

Obiettivo:
1) Crea un grafico (es. sin(x) * exp(-x/10)).
2) Salva in:
   - outputs/ex06_export.png (dpi=300)
   - outputs/ex06_export.pdf

Vincoli:
- Usa fig.savefig(...)
- Usa bbox_inches='tight'
"""

import numpy as np
import matplotlib.pyplot as plt


def main():
    x = np.linspace(0, 10, 250)
    y = np.sin(x) * np.exp(-x/10)

    # TODO: fig, ax

    # TODO: ax.plot + titolo/assi/griglia

    # TODO: export PNG e PDF

    plt.show()


if __name__ == '__main__':
    main()
