"""EX04 - Time series (date + rolling)

Obiettivo:
1) Genera una serie giornaliera di 60 giorni.
2) Calcola una media mobile (rolling window=7).
3) Plotta serie originale + media mobile.
4) Salva in outputs/ex04_timeseries.png.

Suggerimento:
- Usa pandas date_range e Series.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main():
    rng = np.random.default_rng(123)
    dates = pd.date_range('2025-01-01', periods=60, freq='D')
    values = pd.Series(rng.normal(100, 10, len(dates)), index=dates)

    # 1) Media mobile a 7 giorni
    ma7 = values.rolling(window=7).mean()

    # 2) Figura + asse
    fig, ax = plt.subplots(figsize=(10, 5))

    # 3) Plot serie originale + rolling
    ax.plot(values.index, values, label="Valori giornalieri", color="steelblue", alpha=0.7)
    ax.plot(ma7.index, ma7, label="Media mobile (7 giorni)", color="orange", linewidth=2)

    # 4) Titolo, assi, griglia, legenda
    ax.set_title("Time Series con Media Mobile (7 giorni)")
    ax.set_xlabel("Data")
    ax.set_ylabel("Valore")
    ax.grid(True, alpha=0.3)
    ax.legend()

    # 5) Export
    fig.savefig("outputs/ex04_timeseries.png", dpi=150, bbox_inches="tight")

    plt.show()


if __name__ == '__main__':
    main()