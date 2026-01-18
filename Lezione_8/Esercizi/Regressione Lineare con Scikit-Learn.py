# 📦 Importa le librerie necessarie
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# 📊 Dati sintetici: superficie (m²) e prezzo (€)
X = np.array([[50], [80], [100], [120], [150]])  # Area in m²
y = np.array([100000, 160000, 200000, 240000, 300000])  # Prezzo in €

# 🧠 Crea e allena il modello
model = LinearRegression()
model.fit(X, y)

# 🔮 Previsione: quanto vale una casa di 110 m²?
X_new = np.array([[110]])
y_pred = model.predict(X_new)
print(f"Prezzo stimato per 110 m²: €{int(y_pred[0])}")

# 📈 Visualizza i dati e la retta di regressione
plt.scatter(X, y, color='blue', label='Dati reali')
plt.plot(X, model.predict(X), color='red', label='Retta di regressione')
plt.scatter(X_new, y_pred, color='green', label='Previsione (110 m²)')
plt.xlabel('Superficie (m²)')
plt.ylabel('Prezzo (€)')
plt.title('Regressione Lineare: Prezzo vs Superficie')
plt.legend()
plt.grid(True)
plt.show()