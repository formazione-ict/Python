# 📦 Import delle librerie
import numpy as np
from sklearn.linear_model import LinearRegression

# 📊 Dataset sintetico
# X contiene due feature: [superficie, stanze]
X = np.array([
    [80, 3],
    [100, 3],
    [120, 4],
    [150, 4],
    [200, 5]
])

# y contiene il prezzo corrispondente
y = np.array([180000, 220000, 260000, 320000, 400000])

# 🧠 Creazione e addestramento del modello
model = LinearRegression()
model.fit(X, y)

# 🔮 Previsione per una casa di 120 m² e 4 stanze
X_new = np.array([[120, 4]])
y_pred = model.predict(X_new)

print(f"Prezzo stimato: €{int(y_pred[0])}")