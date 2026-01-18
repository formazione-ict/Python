# Esercizio: Regressione Lineare con Scikit-Learn
## Obiettivi didattici
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

1. Crea un modello di regressione lineare multivariata usando scikit‑learn.
2. Allena il modello sui dati forniti.
3. Prevedi il prezzo di una casa con:
- 120 m²
- 4 stanze
4. Visualizza la predizione.

# VERSIONE 1 — Con Train-Test Split
Dividi il dataset in train (70%) e test (30%), allena il modello e valuta l’accuratezza R².

# VERSIONE 2 — Con StandardScaler
Applica lo scaling alle feature prima di addestrare il modello.

# VERSIONE 3 — Con Rumore nei Dati (per mostrare robustezza)
Aggiungi rumore casuale ai prezzi e osserva come cambia la regressione.

# VERSIONE 4 — Con Grafico 3D (superficie + stanze + prezzo)
Visualizza i dati e il piano di regressione in 3D.

# Valutazione Completa (MAE, MSE, RMSE, R²)
Calcola tutte le metriche principali di regressione.
