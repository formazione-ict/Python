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

# Esercizio: Classificare utenti come “premium” o “standard”
## Obiettivo:
Prevedere se un utente è premium (1) o standard (0) in base a:
- Numero di acquisti
- Tempo medio sul sito
- Numero di recensioni lasciate

## Output atteso
🔍 Decision Tree  
Accuracy: 1.0  
              precision    recall  f1-score   support

   0               1.00      1.00      1.00         3  
   1               1.00      1.00      1.00         3

   accuracy                            1.00         6  
   macro avg       1.00      1.00      1.00         6  
weighted avg       1.00      1.00      1.00         6  

🔍 Random Forest  
Accuracy: 1.0  
              precision    recall  f1-score   support

   0               1.00      1.00      1.00         3  
   1               1.00      1.00      1.00         3

   accuracy                            1.00         6  
   macro avg       1.00      1.00      1.00         6  
weighted avg       1.00      1.00      1.00         6

## Estensioni didattiche
- Aggiungi train-test split per valutare la generalizzazione
- Visualizza l’albero con plot_tree (se vuoi interpretabilità)
- Usa predict_proba per analizzare la sicurezza delle predizioni
- Introduci noise per mostrare la fragilità del Decision Tree

# Esercizio: Raggruppare utenti in base a comportamento
## Obiettivo
Raggruppare utenti in base a:
- Tempo medio sul sito
- Numero di pagine visitate
Non abbiamo etichette (y), quindi usiamo K-Means per scoprire gruppi nascosti.

## Output atteso
Tre gruppi ben separati:
- Utenti brevi e poco attivi
- Utenti medi
- Utenti molto attivi

# Esercizio: Riduzione dimensionale con PCA
## Obiettivo
Hai un dataset con 5 feature. Vuoi:
- Ridurre a 2 componenti principali
- Visualizzare i dati ridotti
- Analizzare quanta varianza viene mantenuta

## Estensioni didattiche
- Aumenta `n_components` per vedere come cresce la varianza mantenuta
- Visualizza la curva cumulativa con `PCA(n_components=None)`
- Usa `load_digits` o `load_iris` per dataset reali
- Confronta PCA con `TruncatedSVD` o `t-SNE` per dati non lineari

# Esercizio: Classificare email come spam o non spam
## Obiettivo
Hai un modello che classifica email:
- 1 = spam
- 0 = non spam
Vuoi confrontare le predizioni con le etichette reali e calcolare tutte le metriche.

## Interpretazione didattica
| Metrica | Significato |
|----------|-----------------------------------|
| Accuracy | 75% delle predizioni sono corrette | 
| Precision | 75% delle email classificate come spam erano davvero spam | 
| Recall | Il modello ha trovato il 60% degli spam reali | 
| F1 Score | Bilancia precisione e copertura | 
| Confusion Matrix | Mostra errori e successi per ogni classe | 

# Esercizio: Valutare un modello con due strategie
## Obiettivo
Confrontare:
- Train-Test Split → una sola divisione
- K-Fold Cross-Validation → valutazione più robusta

## Estensioni possibili
- Usa StratifiedKFold per classi sbilanciate
- Calcola anche precision, recall, f1 per ogni fold
- Visualizza la distribuzione degli score con matplotlib

# Esercizio: Ottimizzare Random Forest con GridSearchCV
## Obiettivo
- Allenare un modello Random Forest
- Ottimizzare gli iperparametri `n_estimators` e `max_depth`
- Valutare il miglior modello trovato

## Estensioni didattiche
- Usa `StratifiedKFold` per classi sbilanciate
- Aggiungi `scoring='f1'` per ottimizzare metriche diverse
- Visualizza la matrice dei risultati con `pandas.DataFrame(grid.cv_results_)`
- Confronta con `RandomizedSearchCV` per tuning più veloce

# Esercizio: Diagnosi del fitting di un modello
## Obiettivo
Confrontare tre modelli:
- Underfitting → troppo semplice
- Giusto → bilanciato
- Overfitting → troppo complesso

# Esercizio: Valutazione di un Modello
## Obiettivo
- Usa le metriche avanzate per valutare un classificatore binario.

## Istruzioni
1. Carica un dataset binario (es. breast_cancer da sklearn.datasets).
2. Dividi in X_train, X_test, y_train, y_test.
3. Addestra un modello (es. LogisticRegression).
4. Calcola le metriche:
    - accuracy
    - precision
    - recall
    - f1_score
    - roc_auc_score
5. Visualizza la matrice di confusione.

## Domande
- Quale metrica è più alta?
- Il modello è più preciso o più sensibile?
- Come potresti migliorare il modello?
