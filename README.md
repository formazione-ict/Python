# CORSO SVILUPPO APPLICAZIONI E ANALISI DATI CON PYTHON

Per iniziare:
1. Download Python install manager da https://www.python.org/downloads/
2. Nel terminale digita
   ```py```
4. Per uscire da Python digitare
   ```exit```

5. TOP 10 LIBRERIE PYTHON

**NUMPY**
- Cos'è: Libreria per il calcolo numerico e gli array.
- Perché: Operazioni veloci su grandi dataset e matrici.
- Come aiuta: Rende i calcoli matematici e l'elaborazione dei dati estremamente veloci.
**PANDAS**
- Cos'è: Libreria per l'analisi e la manipolazione dei dati.
- Perché: Facile gestione di file CSV, Excel e database.
- Come aiuta: Pulisce, filtra e analizza i dati in poche righe di codice.
**MATPLOTLIB**
- Cos'è: Libreria per la visualizzazione dei dati.
- Perché: Creare grafici e diagrammi.
- Come aiuta: Trasforma dati grezzi in informazioni visive.
**SEABORN**
- Cos'è: Libreria avanzata per la visualizzazione basata su Matplotlib.
- Perché: Grafici statistici dall'aspetto migliore.
- Come aiuta: Permette di creare grafici professionali e puliti con facilità.
**SCIKIT-LEARN**
- Cos'è: Libreria per il machine learning.
- Perché: Costruire modelli di machine learning facilmente.
- Come aiuta: Fornisce algoritmi pronti per previsioni e classificazioni.
**TENSORFLOW**
- Cos'è: Framework per il deep learning.
- Perché: Per reti neurali e modelli di intelligenza artificiale.
- Come aiuta: Alimenta sistemi di riconoscimento delle immagini, elaborazione del linguaggio naturale e sistemi di raccomandazione.
**PYTORCH**
- Cos'è: Libreria per il deep learning.
- Perché: Flessibile e adatta alla ricerca.
- Come aiuta: Utilizzata per addestrare modelli di intelligenza artificiale avanzati con facilità.
**OPENCV**
- Cos'è: Libreria per la visione artificiale.
- Perché: Elaborazione di immagini e video.
- Come aiuta: Abilita il riconoscimento facciale, il tracciamento di oggetti e l'applicazione di filtri.
   
6. Installare i pacchetti direttamente nel terminale e non in Python
```py -m pip install numpy
py -m pip install matplotlib
py -m pip install jupyterlab pandas
py -m pip install seaborn
py -m pip install notebook
py -m pip install scipy
py -m pip install black
py -m pip install ipywidgets
py -m pip install pytest
py -m pip install requests
```
7. Verifica se JupyterLab funziona. Dopo l’installazione, prova:
```py -m jupyterlab ```
Se si apre il browser, tutto è ok. Nel terminale fai Control + c per uscire
8. Verifica di Pandas. Nel terminale digita ```py``` per entrare in Python:
```import pandas as pd```
```print(pd.__version__)```

9. Altra verifica con codice:
```
import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame({
    "Nome": ["Anna", "Luca", "Marco"],
    "Età": [23, 30, 27]
})

df["Età"].plot(kind="bar")
plt.show()
```
