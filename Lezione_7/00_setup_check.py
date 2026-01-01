"""
00 - Setup check
Scopo: verificare che Matplotlib sia installato e che l'import funzioni.
"""

import matplotlib
import matplotlib.pyplot as plt

def main():
    print("Matplotlib version:", matplotlib.__version__)

    # Mini-plot “smoke test”
    fig, ax = plt.subplots()
    ax.plot([0, 1, 2], [0, 1, 0])
    ax.set_title("Setup OK")
    plt.show()

if __name__ == "__main__":
    main()
