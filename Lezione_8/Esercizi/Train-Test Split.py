import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

X = np.array([
    [80, 3],
    [100, 3],
    [120, 4],
    [150, 4],
    [200, 5]
])

y = np.array([180000, 220000, 260000, 320000, 400000])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("R²:", r2_score(y_test, y_pred))