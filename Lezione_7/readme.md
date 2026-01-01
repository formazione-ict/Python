#Struttura della repo

matplotlib-corso/

├── readme.md

├── requirements.txt

├── .gitignore

├── lessons/

│   ├── 00_setup_check.py

│   ├── 01_quickstart_oo.py

│   ├── 02_linee_stile_legend.py

│   ├── 03_subplots_dashboard.py

│   ├── 04_timeseries_date_formatter.py

│   ├── 05_heatmap_imshow.py

│   └── 06_export_savefig.py

├── exercises/

│   ├── ex01_line_plot.py

│   ├── ex02_bar_chart.py

│   ├── ex03_subplots_2x2.py

│   ├── ex04_timeseries.py

│   ├── ex05_heatmap.py

│   └── ex06_export.py

├── solutions/

│   ├── ex01_line_plot_solution.py

│   ├── ex02_bar_chart_solution.py

│   ├── ex03_subplots_2x2_solution.py

│   ├── ex04_timeseries_solution.py

│   ├── ex05_heatmap_solution.py

│   └── ex06_export_solution.py

└── outputs/

    └── .gitkeep


#Software e setup di sviluppo

Installazione via pip: python -m pip install -U pip e python -m pip install -U matplotlib (opzionale anche Jupyter/IPython per lavorare in notebook).

​
In Matplotlib è comune creare grafici con lo stile “object-oriented” usando fig, ax = plt.subplots() e poi chiamando i metodi su ax.
​
