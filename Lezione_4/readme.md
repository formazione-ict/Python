Struttura completa e modulare

Ho diviso gli argomenti in 5 notebook progressivi (.ipynb) per facilitare l'apprendimento passo-passo, più un file di dati di esempio.

📂 Struttura del Repository

corso-python-pandas/

│

├── data/

│   └── vendite_sample.csv             # Dataset di esempio (generato nello script)

│

├── 01_intro_pandas_series.ipynb       # Basi: Series e creazione DataFrame

├── 02_selezione_filtraggio.ipynb      # loc, iloc e filtri condizionali

├── 03_manipolazione_dati.ipynb        # Pulizia, nuove colonne, gestione Null

├── 04_groupby_aggregazioni.ipynb      # Analisi avanzata: group by, pivot

├── 05_progetto_vendite.ipynb          # Capstone Project completo

├── README.md                          # Istruzioni

└── requirements.txt                   # Dipendenze

Consigli per l'uso

1. Dati Reali: Nel progetto finale, puoi sostituire la creazione del dataset finto con df = pd.read_csv('tuo_file.csv').
2. Dataset Sample: Se vuoi fornire un CSV fisico, puoi eseguire il primo blocco del notebook 5 e poi salvare il risultato con to_csv.
3. Jupyter Lab: È l'ambiente ideale. Basta lanciare jupyter lab nella cartella e aprire i file .ipynb.
