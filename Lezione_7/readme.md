# Corso Matplotlib (Python)

Repository didattico per imparare Matplotlib tramite:
- lezioni progressive (cartella `Lezioni/`)
- esercizi (cartella `Esercizi/`)
- soluzioni (cartella `Soluzioni/`)
- output esportati (cartella `Outputs/`)

## Software consigliato
- Python 3.10+ (consigliato 3.11 o 3.12)
- IDE: VS Code (Python + Pylance) oppure PyCharm
- Opzionale: Jupyter Notebook / JupyterLab per demo live

## Setup ambiente (venv)
### Windows (PowerShell)
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -U pip
pip install -r requirements.txt
```
### macOS / Linux (bash/zsh)
```powershell
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
pip install -r requirements.txt
```
Nota: per installare Matplotlib con pip, la documentazione ufficiale usa:
python -m pip install -U pip e python -m pip install -U matplotlib (opzionale anche Jupyter/IPython per lavorare in notebook)

# Struttura della repo

matplotlib-corso/

├── readme.md

├── requirements.txt

├── .gitignore

├── Lezioni/

│   ├── 00_setup_check.py

│   ├── 01_quickstart_oo.py

│   ├── 02_linee_stile_legend.py

│   ├── 03_subplots_dashboard.py

│   ├── 04_timeseries_date_formatter.py

│   ├── 05_heatmap_imshow.py

│   └── 06_export_savefig.py

├── Esercizi/

│   ├── ex01_line_plot.py

│   ├── ex02_bar_chart.py

│   ├── ex03_subplots_2x2.py

│   ├── ex04_timeseries.py

│   ├── ex05_heatmap.py

│   └── ex06_export.py

├── Soluzioni/

│   ├── ex01_line_plot_solution.py

│   ├── ex02_bar_chart_solution.py

│   ├── ex03_subplots_2x2_solution.py

│   ├── ex04_timeseries_solution.py

│   ├── ex05_heatmap_solution.py

│   └── ex06_export_solution.py

└── Outputs/

    └── .gitkeep

In Matplotlib è comune creare grafici con lo stile “object-oriented” usando fig, ax = plt.subplots() e poi chiamando i metodi su ax.

# Esecuzione
## Esegui uno script:
python lessons/01_quickstart_oo.py

## Esegui un esercizio:
python exercises/ex03_subplots_2x2.py

## Regole per gli esercizi
Non modificare i file in solutions/ (sono la chiave).

Gli script degli esercizi devono:
1. generare il grafico
2. aggiungere titolo/assi/griglia
3. (se richiesto) salvare in outputs/

# Export figure (salvataggio)
Per salvare figure usare fig.savefig(...), ad esempio:

fig.savefig("outputs/grafico.png", dpi=300, bbox_inches="tight")

- Il formato può essere dedotto dall’estensione del filename (es. .png, .pdf, .svg).
- dpi aiuta a esportare PNG ad alta risoluzione.
- bbox_inches="tight" riduce i margini bianchi.​

# Note
Le istruzioni di installazione via pip mostrate nel README sono quelle indicate nella documentazione ufficiale di Matplotlib.
​
Le note su savefig() (formato dedotto dall’estensione e parametri come dpi/bbox_inches) sono coerenti con l’API documentata per matplotlib.pyplot.savefig.
