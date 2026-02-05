# Scikit-learn Pipelines con Titanic

In questo tutorial vedremo come costruire pipeline di Machine Learning con Scikit-learn. Pipeline è un modo per concatenare diverse operazioni in un oggetto pratico, quasi come un wrapper. 
Questo astrae molte singole operazioni che altrimenti potrebbero apparire frammentate nello script. 

## Setup
In questo tutorial utilizzeremo il dataset di Titanic, materiale didattico di Kaggle 101 (Competizioni di Data Science). 
Per prima cosa, importiamo i moduli e i dataset necessari. 

### Importazione di dipendenze
Scikit-learn è la libreria di riferimento per l'apprendimento automatico in Python. Contiene non solo utilità di caricamento dati, ma anche inputer, encoder, pipeline, trasformatori e strumenti di ricerca di cui avremo bisogno per trovare il modello ottimale per l'attività.
```
import numpy as np

from sklearn.compose import ColumnTransformer
from sklearn.datasets import fetch_openml
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.preprocessing import RobustScaler, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score, RandomizedSearchCV
```
### Caricamento dei dati
Carichiamo il set di dati utilizzando `fetch_openml`.
```
np.random.seed(42)

X, y = fetch_openml("titanic", version=1, as_frame=True, return_X_y=True)
X.drop(['boat', 'body', 'home.dest'], axis=1, inplace=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2)
```
Osserviamo i dati chiamando `.head()`. Per impostazione predefinita, questa funzione mostra le prime cinque righe e tutte le colonne che possono essere inserite nel notebook.

```X_train.head()```
| pclass | name                                               | sex    | age  | sibsp | parch | ticket         | fare    | cabin | embarked |
|--------|----------------------------------------------------|--------|------|-------|-------|----------------|---------|-------|----------|
| 3.0    | McCarthy, Miss. Catherine 'Katie'                  | female | NaN  | 0.0   | 0.0   | 383123         | 7.7500  | None  | Q        |
| 2.0    | del Carlo, Mrs. Sebastiano (Argenia Genovesi)      | female | 24.0 | 1.0   | 0.0   | SC/PARIS 2167  | 27.7208 | None  | C        |
| 3.0    | Andersson, Miss. Sigrid Elisabeth                  | female | 11.0 | 4.0   | 2.0   | 347082         | 31.2750 | None  | S        |
| 3.0    | Saad, Mr. Khalil                                   | male   | 25.0 | 0.0   | 0.0   | 2672           | 7.2250  | None  | C        |
| 3.0    | Abelseth, Miss. Karen Marie                        | female | 16.0 | 0.0   | 0.0   | 348125         | 7.6500  | None  | S        |

## Esplorazione dei dati
Esaminiamo i dati più in dettaglio per gettare le basi per la nostra analisi. Questa fase in genere prevede i seguenti passaggi:
- Verifica della presenza di voci nulle
- Identificazione della covarianza
- Feature Engineering

### Valori mancanti
Prima di procedere con qualsiasi analisi dei dati, è sempre una buona idea prestare attenzione ai valori mancanti: quanti sono, dove si verificano, ecc. Diamo un'occhiata.

```X_train.isnull().any()```

|-----------|---------------|
| pclass    | False         |
| name      | False         |
| sex       | False         |
| age       | True          |
| sibsp     | False         |
| parch     | False         |
| ticket    | False         |
| fare      | True          |
| cabin     | True          |
| embarked  | False         |
dtype: bool

La funzione `any()` è utile, ma non ci mostra realmente quanti valori mancano per ogni colonna. Per approfondire questo problema, dobbiamo usare invece `sum()`.

```X_train.isnull().sum()```
|-----------|-----------|
| pclass    | 0         |
| name      | 0         |
| sex       | 0         |
| age       | 209       |
| sibsp     | 0         |
| parch     | 0         |
| ticket    | 0         |
| fare      | 1         |
| cabin     | 822       |
| embarked  | 0         |
dtype: int64

Esiste anche una libreria di visualizzazione dati molto interessante chiamata *missingno*, che consente di osservare i dati mancanti.

```
import missingno as msno
import matplotlib.pyplot as plt
%matplotlib inline
%config InlineBackend.figure_format = 'png'

msno.matrix(X_train)
plt.show()
```
<img width="1485" height="644" alt="image" src="https://github.com/user-attachments/assets/d2afbfe7-b597-4bc6-bf1b-10ccd014de22" />

Questa visualizzazione ci fornisce un'idea più intuitiva di dove si trovano i valori mancanti. 
In questo caso, i valori mancanti sembrano essere distribuiti in modo piuttosto uniforme o casuale. 
Tuttavia, possiamo anche immaginare casi in cui i valori mancanti potrebbero avere a che fare con un attributo intrinseco nel set di dati (ad esempio, solo i partecipanti maschi di un sondaggio potrebbero rispondere "N/D" a un questionario sanitario che include domande sulla gravidanza). 
In questi casi, utilizzare questa libreria per visualizzare dove si trovano i valori mancanti è una buona idea, poiché si tratta di una dimensione informativa aggiuntiva che la chiamata a `df.isnull().sum()` non sarebbe in grado di rivelare.

Ora che abbiamo un'idea approssimativa di dove si trovano i valori mancanti, dobbiamo scegliere tra una delle seguenti opzioni:
- Eliminare le voci con valori mancanti
- Eliminare le colonne con troppi valori mancanti
- Utilizzare l'imputazione per riempire i valori mancanti con valori alternativi
In effetti, in questo caso, procederemo eliminando l'attributo "cabina". Questa scelta diventa più ovvia quando calcoliamo la percentuale di valori nulli.

```X_train.isnull().sum() / len(X_train) * 100```
|-----------|------------------|
| pclass    | 0.000000         |
| name      | 0.000000         |
| sex       | 0.000000         |
| age       | 19.961796        |
| sibsp     | 0.000000         |
| parch     | 0.000000         |
| ticket    | 0.000000         |
| fare      | 0.095511         |
| cabin     | 78.510029        |
| embarked  | 0.000000         |
dtype: float64

Questo ci mostra che il 78.51% delle righe presenta valori mancanti per gli attributi della cabina. 
Date queste informazioni, probabilmente è una cattiva idea cercare di imputare questi valori. Scegliamo di eliminarli.

`X_train.drop(['cabin'], axis=1, inplace=True)
X_test.drop(['cabin'], axis=1, inplace=True)`

### Correlazione
La correlazione (o, in modo più o meno equivalente, la covarianza) è una metrica di cui teniamo sempre conto, poiché l'obiettivo finale dell'ingegneria del machine learning è utilizzare un insieme di caratteristiche di input per generare una previsione. In questo contesto, non vogliamo fornire al nostro modello informazioni inutili e prive di valore; vogliamo invece immettere nel modello solo caratteristiche altamente correlate, rilevanti e informative. Se alcune caratteristiche nei dati grezzi sono ritenute inutili, dobbiamo eliminarle o impegnarci in una sorta di ingegneria delle caratteristiche per produrre un nuovo insieme di caratteristiche più correlate.

```
import pandas as pd
import seaborn as sns
%config InlineBackend.figure_format = 'svg'

X_comb = pd.concat([X_train, y_train.astype(float)], axis=1)
g = sns.heatmap(X_comb[['pclass', 'sex', 'age', 'sibsp', 'parch', 'fare', 'survived']].corr(),
                annot=True, 
                cmap = "coolwarm")
```

<img width="477" height="342" alt="image" src="https://github.com/user-attachments/assets/f1c5c09c-5daa-4786-8b40-5022a707fd15" />

Da questa analisi preliminare, sembra che ci siano alcune feature correlate molto settimanalmente, ovvero "parch" e "sibsp". La correlazione settimanale suggerisce che forse dovremmo impegnarci in un po' di "feature engineering" per estrarre informazioni più significative dal dataset.

## Feature Engineering
Utilizziamo i risultati della sezione precedente per progettare alcune feature più informative. Un approccio popolare è quello di utilizzare i nomi per derivare una feature titolo. Intuitivamente, questo ha senso: Sig. e Sig.ra, Capitano e Dott. potrebbero essere di interesse per il nostro modello. Un altro approccio popolare è quello di combinare le feature meno importanti, "parch" e "sibsp", in qualcosa come "family_size". L'implementazione di queste dovrebbe essere abbastanza semplice, quindi proviamo qui.

Si noti che in un contesto reale, non ci sarà alcuna risposta al riferimento; dovremo fare affidamento sulla nostra conoscenza del dominio e su un'EDA più ampia per capire quali feature sono importanti e di quali nuove feature avremo bisogno.

### Family
A volte, feature debolmente correlate possono essere combinate insieme per formare una nuova feature, che potrebbe presentare una correlazione più elevata rispetto al target. Possiamo combinare parch e sibsp in una nuova feature, chiamata family_size. A rigor di termini, dovremmo aggiungere 1, ma aggiungere tutti i valori di uno equivale a spostare tutto di un valore costante, il che non influirà sulla modellazione, poiché tali aggiustamenti costanti saranno comunque gestiti dalla fase di pre-elaborazione.

Si noti che l'ingegneria delle feature viene applicata simultaneamente sia al set di addestramento che a quello di test.

```
for dataset in [X_train, X_test]:
    dataset['family_size'] = dataset['parch'] + dataset['sibsp']
    dataset.drop(['parch', 'sibsp'], axis=1, inplace=True)
    dataset['is_alone'] = 1
    dataset['is_alone'].loc[dataset['family_size'] > 1] = 0

X_train.head()
```

| pclass | name                                               | sex    | age  | ticket         | fare    | embarked | family_size | is_alone |
|--------|----------------------------------------------------|--------|------|----------------|---------|----------|-------------|----------|
| 3.0    | McCarthy, Miss. Catherine 'Katie'                  | female | NaN  | 383123         | 7.7500  | Q        | 0.0         | 1        |
| 2.0    | del Carlo, Mrs. Sebastiano (Argenia Genovesi)      | female | 24.0 | SC/PARIS 2167  | 27.7208 | C        | 1.0         | 1        |
| 3.0    | Andersson, Miss. Sigrid Elisabeth                  | female | 11.0 | 347082         | 31.2750 | S        | 6.0         | 0        |
| 3.0    | Saad, Mr. Khalil                                   | male   | 25.0 | 2672           | 7.2250  | C        | 0.0         | 1        |
| 3.0    | Abelseth, Miss. Karen Marie                        | female | 16.0 | 348125         | 7.6500  | S        | 0.0         | 1        |

### Title
Abbiamo creato due nuove funzionalità, ovvero `family_size` e `is_alone`. 
Procediamo con l'engineering delle funzionalità anche sulla colonna *name* per estrarre più informazioni.

```
for dataset in [X_train, X_test]:
  dataset['title'] =  dataset['name'].str.split(", ", expand=True)[1].str.split(".", expand=True)[0]
  dataset.drop(["name"], axis=1, inplace=True)

X_train.head()
```

| pclass | sex    | age  | ticket         | fare    | embarked | family_size | is_alone | title |
|--------|--------|------|----------------|---------|----------|-------------|----------|--------|
| 3.0    | female | NaN  | 383123         | 7.7500  | Q        | 0.0         | 1        | Miss   |
| 2.0    | female | 24.0 | SC/PARIS 2167  | 27.7208 | C        | 1.0         | 1        | Mrs    |
| 3.0    | female | 11.0 | 347082         | 31.2750 | S        | 6.0         | 0        | Miss   |
| 3.0    | male   | 25.0 | 2672           | 7.2250  | C        | 0.0         | 1        | Mr     |
| 3.0    | female | 16.0 | 348125         | 7.6500  | S        | 0.0         | 1        | Miss   |

Ora abbiamo alcuni dati che sembrano molto più gestibili. 
Tuttavia, abbiamo ancora un problema con la colonna del titolo: sembra che ci siano molti titoli, quindi probabilmente dovremmo effettuare un po' di binning o raggruppamento.

```pd.crosstab(X_train['title'], X_train['sex'])```

| sex           | female | male |
|---------------|--------|------|
| title         |        |      |
|---------------|--------|------|
| Capt          | 0      | 1    |
| Col           | 0      | 3    |
| Don           | 0      | 1    |
| Dona          | 1      | 0    |
| Dr            | 0      | 6    |
| Major         | 0      | 1    |
| Master        | 0      | 51   |
| Miss          | 210    | 0    |
| Mlle          | 2      | 0    |
| Mr            | 0      | 606  |
| Mrs           | 156    | 0    |
| Ms            | 2      | 0    |
| Rev           | 0      | 6    |
| the Countess  | 1      | 0    |








