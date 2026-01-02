"""
06 - Export: PNG/PDF/SVG con savefig
Scopo: generare un grafico e salvarlo in più formati.
"""

import numpy as np
import matplotlib.pyplot as plt

def main():
    x = np.linspace(0, 10, 200)
    y = np.sin(x) * np.exp(-x/10)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x, y, linewidth=2)
    ax.set_title("Export demo")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True, alpha=0.25)

    # Suggerimento pratico: bbox_inches="tight" riduce bordi “vuoti”
    fig.savefig("output_demo.png", dpi=300, bbox_inches="tight")
    fig.savefig("output_demo.pdf", bbox_inches="tight")
    fig.savefig("output_demo.svg", bbox_inches="tight")

    plt.show()

if __name__ == "__main__":
    main()
