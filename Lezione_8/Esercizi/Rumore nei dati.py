import numpy as np
from sklearn.linear_model import LinearRegression

rng = np.random.default_rng(42)

X = np.array([
    [80, 3],
    [100, 3],
    [120, 4],
    [150, 4],
    [200, 5]
])

y = np.array([180000, 220000, 260000, 320000, 400000])

rumore = rng.normal(0, 15000, size=y.shape)
y_noisy = y + rumore

model = LinearRegression()
model.fit(X, y_noisy)

X_new = np.array([[120, 4]])
y_pred = model.predict(X_new)

print(f"Prezzo stimato con rumore: €{int(y_pred[0])}")