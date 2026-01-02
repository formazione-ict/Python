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

    # 1) Figura e asse
    fig, ax = plt.subplots(figsize=(8, 4))

    # 2) Plot + titolo/assi/griglia
    ax.plot(x, y, color="purple", linewidth=2)
    ax.set_title("sin(x) * exp(-x/10)")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True, alpha=0.3)

    # 3) Export PNG e PDF
    fig.savefig("outputs/ex06_export.png", dpi=300, bbox_inches="tight")
    fig.savefig("outputs/ex06_export.pdf", bbox_inches="tight")

    plt.show()


if __name__ == '__main__':
    main()
