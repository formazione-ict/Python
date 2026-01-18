import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

X = np.array([
    [80, 3],
    [100, 3],
    [120, 4],
    [150, 4],
    [200, 5]
])

y = np.array([180000, 220000, 260000, 320000, 400000])

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = LinearRegression()
model.fit(X_scaled, y)

X_new = np.array([[120, 4]])
X_new_scaled = scaler.transform(X_new)

y_pred = model.predict(X_new_scaled)
print(f"Prezzo stimato (scaled): €{int(y_pred[0])}")