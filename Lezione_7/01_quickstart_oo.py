"""
01 - Quickstart (OO style)
Scopo: capire Figure/Axes e il flusso tipico:
1) crei fig, ax
2) disegni su ax
3) mostri con plt.show()
"""

import matplotlib.pyplot as plt

def main():
    # 1) Figure + singolo Axes
    fig, ax = plt.subplots()

    # 2) Disegno sul solo Axes
    x = [1, 2, 3, 4]
    y = [1, 4, 2, 3]
    ax.plot(x, y, marker="o", label="Serie A")

    ax.set_title("Primo grafico con Matplotlib")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    ax.grid(True, alpha=0.3)

    # 3) Mostra
    plt.show()

if __name__ == "__main__":
    main()
