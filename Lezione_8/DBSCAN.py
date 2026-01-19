import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

# 1. Creazione dati X (Feature Space)
# Generiamo dati casuali per simulare il comportamento degli utenti
np.random.seed(42)
X = np.random.rand(100, 2) * [1000, 20] # Tempo fino a 1000s, Pagine fino a 20

# 2. PREPROCESS - Scaling
# Senza questo, DBSCAN fallirebbe a causa delle diverse unità di misura
X_scaled = StandardScaler().fit_transform(X)

# 3. MODELLO DBSCAN (Unsupervised Learning)
# Usiamo eps=0.5 perché i dati ora sono scalati (media 0, varianza 1)
dbscan = DBSCAN(eps=0.5, min_samples=5)
db_clusters = dbscan.fit_predict(X_scaled)

# 4. VISUALIZZAZIONE
plt.figure(figsize=(10, 6))
scatter = plt.scatter(X[:, 0], X[:, 1], c=db_clusters, cmap='plasma')
plt.title("DBSCAN Clustering: Identificazione gruppi e Outlier (-1)")
plt.xlabel("Tempo sul sito (secondi)")
plt.ylabel("Pagine visitate")
plt.colorbar(scatter, label='ID Cluster')
plt.grid(True)
plt.show()