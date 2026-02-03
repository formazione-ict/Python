import pandas as pd

from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Carica dataset
diabetes = load_diabetes(as_frame=True)
X = diabetes.data        # 10 feature numeriche
y = diabetes.target

# 2. Train/Test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Genera feature polinomiali (grado 2)
poly = PolynomialFeatures(degree=2, include_bias=False)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

print("Shape originale:", X_train.shape)         # (n, 10)
print("Shape polinomiale:", X_train_poly.shape)  # (n, molte più colonne)

# 4. Regressione lineare sulle feature polinomiali
poly_reg = LinearRegression()
poly_reg.fit(X_train_poly, y_train)

# 5. Valutazione
y_pred_poly = poly_reg.predict(X_test_poly)
mse_poly = mean_squared_error(y_test, y_pred_poly)
r2_poly = r2_score(y_test, y_pred_poly)

print(f"Polynomial Regression (deg=2) MSE: {mse_poly:.2f}")
print(f"Polynomial Regression (deg=2) R2:  {r2_poly:.3f}")
