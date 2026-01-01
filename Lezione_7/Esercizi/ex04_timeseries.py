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

    # TODO: ma7 = values.rolling(window=7).mean()

    # TODO: fig, ax + plot di values e ma7

    # TODO: titolo/assi/griglia/legenda

    # TODO: export

    plt.show()


if __name__ == '__main__':
    main()
