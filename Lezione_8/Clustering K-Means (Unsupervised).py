import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler # Per lo Scaling

# 1. GENERAZIONE DATI (Creazione della variabile X)
# Creiamo 300 punti casuali in uno spazio 2D
X = np.random.randn(300, 2) 

# 2. PREPROCESS - Scaling
# Lo scaling è fondamentale per il KMeans perché si basa sulla distanza euclidea
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  # Applichiamo il scaler ai dati

# 3. MODELLO
model = KMeans(n_clusters=3,        # Crea un modello con 3 cluster
               random_state=42)     # 42 serve per rendere il risultato ripetibile
clusters = model.fit_predict(X_scaled)  # Applichiamo il modello ai dati scalati
                                        # Niente etichette y! è unsupervised learning
# 4. VISUALIZZAZIONE
# Recuperiamo i centri dei cluster (centroidi)
centers = model.cluster_centers_

plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=clusters, cmap='viridis') # Visualizza i punti colorati in base al cluster assegnato
plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='X', s=200, label='Centroidi')    # Mostra i centroidi dei cluster con una X rossa
plt.title("Clustering K-Means (Unsupervised)")
plt.show()