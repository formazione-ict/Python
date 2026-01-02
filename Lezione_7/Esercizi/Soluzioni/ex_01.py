"""Soluzione Esercizio 01 - Line plot (2 serie)

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

    # 1) Crea fig e ax (OO API)
    fig, ax = plt.subplots(figsize=(8, 4))

    # 2) Disegna le due linee
    ax.plot(x, y1, color='blue', label='sin(x)')
    ax.plot(x, y2, color='red', linestyle='--', label='cos(x)')

    # 3) Titolo, assi, griglia, legenda
    ax.set_title("Seno e Coseno")
    ax.set_xlabel("x (rad)")
    ax.set_ylabel("valore")
    ax.grid(True, alpha=0.3)
    ax.legend()

    # 4) Salvataggio
    fig.savefig('outputs/ex01_line_plot.png', dpi=150, bbox_inches='tight')

    plt.show()


if __name__ == '__main__':
    main()
