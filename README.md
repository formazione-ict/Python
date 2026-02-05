# CORSO SVILUPPO APPLICAZIONI E ANALISI DATI CON PYTHON

## PROGRAMMA
1.	Fondamenti di Python: Strutture dati, Liste
2.	Dizionari, Stringhe e file, Funzioni
3.	Jupyter: notebook per lo sviluppo di progetti python
4.	Pandas: strutture dati e operazioni base
5.	Pandas: filtri, merge, operazioni aggiuntive
6.	Programmazione ad oggetti in Python
7.	Matplotlib: libreria per la creazione di grafici
8.	Concetti di Machine learning
9.	Sklearn open source di apprendimento automatico 
10.	Sklearn classificazione e regressione
11.	Integrazione con moduli esterni in C, C++, Java

## CONOSCENZE
- Strumenti di sviluppo
- Tecniche di programmazione strutturata
- Tecniche di programmazione ad oggetti
- Linguaggi di programmazione imperativi
- Linguaggi di programmazione ad oggetti
- Tipologie di applicazioni
- Tecniche di debugging
- Metodi di collaudo di procedure e applicazioni

## ABILITÀ
-	Utilizzare e integrare componenti reperibili sul mercato
-	Applicare tecniche di collaudo del software
-	Scegliere strumenti di sviluppo in base alle caratteristiche dell’applicazione
-	Applicare tecniche di codifica degli algoritmi
-	Applicare tecniche di documentazione dell’applicazione

## Per iniziare:
1. Download Python install manager da https://www.python.org/downloads/
2. Nel terminale digita
   ```py```
4. Per uscire da Python digitare
   ```exit```

## TOP 10 LIBRERIE PYTHON
(Installare i pacchetti direttamente nel terminale e non in Python)

**NUMPY** `py -m pip install numpy`
- Cos'è: Libreria per il calcolo numerico e gli array.
- Perché: Operazioni veloci su grandi dataset e matrici.
- Come aiuta: Rende i calcoli matematici e l'elaborazione dei dati estremamente veloci.

**PANDAS** `py -m pip install pandas`
- Cos'è: Libreria per l'analisi e la manipolazione dei dati.
- Perché: Facile gestione di file CSV, Excel e database.
- Come aiuta: Pulisce, filtra e analizza i dati in poche righe di codice.

**MATPLOTLIB** `py -m pip install matplotlib`
- Cos'è: Libreria per la visualizzazione dei dati.
- Perché: Creare grafici e diagrammi.
- Come aiuta: Trasforma dati grezzi in informazioni visive.

**SEABORN** `py -m pip install seaborn`
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
   
## Verifica installazione

### Verifica di Pandas. Nel terminale digita ```py``` per entrare in Python:
```import pandas as pd```
```print(pd.__version__)```

### Altra verifica con codice:
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
