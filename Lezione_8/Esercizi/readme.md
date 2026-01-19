# Esercizio: Regressione Lineare con Scikit-Learn
## Obiettivi:
- Capire come funziona la regressione lineare
- Visualizzare la relazione tra variabili
- Interpretare la retta come modello predittivo
- Introdurre il concetto di generalizzazione

## Estensioni possibili
- Aggiungere rumore ai dati per simulare variabilità
- Usare r2_score per valutare la bontà del modello
- Confrontare con modelli non lineari (es. polinomiali)

# Esercizio: Predire il prezzo di una casa usando due feature
Hai un dataset sintetico con:
- Superficie (m²)
- Numero di stanze
- Prezzo (€)
## Obiettivo:
1. Crea un modello di regressione lineare multivariata usando scikit‑learn.
2. Allena il modello sui dati forniti.
3. Prevedi il prezzo di una casa con:
- 120 m²
- 4 stanze
4. Visualizza la predizione.

## Varianti:
### VERSIONE 1 — Con Train-Test Split
Dividi il dataset in train (70%) e test (30%), allena il modello e valuta l’accuratezza R².

### VERSIONE 2 — Con StandardScaler
Applica lo scaling alle feature prima di addestrare il modello.

### VERSIONE 3 — Con Rumore nei Dati (per mostrare robustezza)
Aggiungi rumore casuale ai prezzi e osserva come cambia la regressione.

### VERSIONE 4 — Con Grafico 3D (superficie + stanze + prezzo)
Visualizza i dati e il piano di regressione in 3D.

### Valutazione Completa (MAE, MSE, RMSE, R²)
Calcola tutte le metriche principali di regressione.

# Esercizio: Classificazione Spam con Logistic Regression
## Obiettivo
Prevedere se un messaggio è spam (1) o non spam (0) in base a tre feature:
- Numero di parole sospette
- Numero di link
- Lunghezza del messaggio

## Output atteso
   accuracy                            1.00         6
   macro avg       1.00      1.00      1.00         6
weighted avg       1.00      1.00      1.00         6

Messaggio 1: Probabilità spam = 1.00, Classe predetta = 1
Messaggio 2: Probabilità spam = 0.00, Classe predetta = 0
Messaggio 3: Probabilità spam = 1.00, Classe predetta = 1
Messaggio 4: Probabilità spam = 0.00, Classe predetta = 0
Messaggio 5: Probabilità spam = 1.00, Classe predetta = 1
Messaggio 6: Probabilità spam = 0.00, Classe predetta = 0

## Estensioni didattiche
- Aggiungere train-test split per valutazione realistica
- Usare StandardScaler per normalizzare le feature
- Cambiare la soglia di classificazione (es. spam se prob > 0.7)
- Visualizzare la curva ROC o precision-recall
