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
`X_train.head()`
| pclass | name                                               | sex    | age  | sibsp | parch | ticket         | fare    | cabin | embarked |
|--------|----------------------------------------------------|--------|------|-------|-------|----------------|---------|-------|----------|
| 3.0    | McCarthy, Miss. Catherine 'Katie'                  | female | NaN  | 0.0   | 0.0   | 383123         | 7.7500  | None  | Q        |
| 2.0    | del Carlo, Mrs. Sebastiano (Argenia Genovesi)      | female | 24.0 | 1.0   | 0.0   | SC/PARIS 2167  | 27.7208 | None  | C        |
| 3.0    | Andersson, Miss. Sigrid Elisabeth                  | female | 11.0 | 4.0   | 2.0   | 347082         | 31.2750 | None  | S        |
| 3.0    | Saad, Mr. Khalil                                   | male   | 25.0 | 0.0   | 0.0   | 2672           | 7.2250  | None  | C        |
| 3.0    | Abelseth, Miss. Karen Marie                        | female | 16.0 | 0.0   | 0.0   | 348125         | 7.6500  | None  | S        |
