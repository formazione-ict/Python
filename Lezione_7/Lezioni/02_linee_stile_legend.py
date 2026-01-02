"""
02 - Linee: stili, colori, legenda
Scopo: personalizzare il plot e “raccontare” i dati con etichette.
"""

import numpy as np
import matplotlib.pyplot as plt

def main():
    x = np.linspace(0, 2*np.pi, 200)
    sinx = np.sin(x)
    cosx = np.cos(x)

    fig, ax = plt.subplots(figsize=(8, 4))

    ax.plot(x, sinx, label="sin(x)", color="C0", linewidth=2)
    ax.plot(x, cosx, label="cos(x)", color="C1", linestyle="--", linewidth=2)

    ax.set_title("Seno e Coseno")
    ax.set_xlabel("Angolo (rad)")
    ax.set_ylabel("Valore")
    ax.legend(loc="upper right")
    ax.grid(True, alpha=0.25)

    plt.show()

if __name__ == "__main__":
    main()
