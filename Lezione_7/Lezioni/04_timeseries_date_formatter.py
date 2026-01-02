"""
Esempi avanzati (dashboard, date, heatmap)
04 - Serie temporali con date
Scopo: plottare date sull'asse X e formattarle in modo leggibile.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import ConciseDateFormatter

def main():
    rng = np.random.default_rng(7)

    # Serie oraria di 20 giorni
    dates = pd.date_range("2025-01-01", periods=24*20, freq="H")
    values = np.cumsum(rng.normal(0, 1, len(dates)))

    fig, ax = plt.subplots(figsize=(10, 4), layout="constrained")
    ax.plot(dates, values, linewidth=1.5)

    ax.set_title("Serie temporale (ore) con formattazione date")
    ax.set_xlabel("Data")
    ax.set_ylabel("Valore cumulato")
    ax.grid(True, alpha=0.25)

    # Formatter compatto per date (ottimo per axis densi)
    ax.xaxis.set_major_formatter(ConciseDateFormatter(ax.xaxis.get_major_locator()))

    plt.show()

if __name__ == "__main__":
    main()
