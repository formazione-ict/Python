import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler # Fondamentale per il Preprocess

# 1. GENERAZIONE DATI (Definiamo X con 1000 features)
np.random.seed(42)
X = np.random.randn(100, 1000) # 100 campioni, 1000 variabili

# 2. PREPROCESS - Scaling
# La PCA richiede dati standardizzati (media=0, varianza=1)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. PCA - Dimensionality Reduction
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X_scaled) # Applichiamo ai dati scalati

# 4. ANALISI DEI RISULTATI
print(f'Dimensioni originali: {X.shape}')
print(f'Nuove dimensioni: {X_reduced.shape}')

varianza = pca.explained_variance_ratio_
print(f'Varianza spiegata dalle prime 2 componenti: {varianza}')
print(f'Varianza totale catturata: {np.sum(varianza) * 100:.2f}%')
plt.figure(figsize=(8, 6))
plt.scatter(X_reduced[:, 0], X_reduced[:, 1], alpha=0.7)
plt.title("Visualizzazione 2D di un dataset a 1000 dimensioni")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.grid(True)
plt.show()