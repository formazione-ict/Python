# 📦 Importa le librerie
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# 📊 Dataset sintetico: 100 esempi, 5 feature
rng = np.random.default_rng(42)
X = rng.normal(0, 1, size=(100, 5))

# ⚖️ Scaling: PCA è sensibile alla scala
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 🧠 PCA: riduci a 2 componenti
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X_scaled)

# 📈 Visualizza i dati ridotti
plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c='blue', alpha=0.6)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("PCA: Riduzione a 2 componenti")
plt.grid(True)
plt.show()

# 📊 Varianza spiegata
explained = pca.explained_variance_ratio_
print(f"Varianza spiegata: {explained}")
print(f"Totale mantenuto: {explained.sum()*100:.2f}%")