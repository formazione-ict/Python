# Standardizzazione delle feature con StandardScaler

# 1. IMPORT E CARICAMENTO DATI
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("dataset.csv")

# Separazione feature/target
X = df.drop("target", axis=1)
y = df["target"]

# 2. TRAIN/TEST SPLIT
# Supponiamo che X sia la matrice delle feature e y il target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. STANDARDIZZAZIONE
scaler = StandardScaler()	# trasforma ogni feature per avere media 0 e deviazione standard 1

# Fit sul train + transform
X_train_scaled = scaler.fit_transform(X_train)	# fit calcola media e deviazione standard sul train; transform applica la formula di scaling ai dati di train

# Transform sul test
X_test_scaled = scaler.transform(X_test)	    # applica lo stesso scaling ai dati di test, usando le statistiche calcolate sul train

# Statistiche apprese dal train
print(f'Mean: {scaler.mean_}')
print(f'Std: {scaler.scale_}')
