# Scikit-learn Pipelines con Titanic

In questo tutorial vedremo come costruire pipeline di Machine Learning con Scikit-learn. Pipeline è un modo per concatenare diverse operazioni in un oggetto pratico, quasi come un wrapper. 
Questo astrae molte singole operazioni che altrimenti potrebbero apparire frammentate nello script. 

## Setup
In questo tutorial utilizzeremo il dataset di Titanic, materiale didattico di Kaggle 101 (Competizioni di Data Science). 
Per prima cosa, importiamo i moduli e i dataset necessari. 

##Importazione di dipendenze
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
