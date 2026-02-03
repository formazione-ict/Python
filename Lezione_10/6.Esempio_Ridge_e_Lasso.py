# 1. Importa librerie
import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge, Lasso, RidgeCV, LassoCV
from sklearn.metrics import mean_squared_error, r2_score

# 2. Carica il dataset diabetes
diabetes = load_diabetes(as_frame=True)   # X e y come DataFrame/Series [web:368]
X = diabetes.data        # 10 feature numeriche
y = diabetes.target      # target continuo (progressione diabete)

# 3. Train/Test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Training e valutazione base di modelli di Ridge e Lasso

# Ridge
ridge = Ridge(alpha=1.0)
ridge.fit(X_train, y_train)

y_pred_ridge = ridge.predict(X_test)
print("Ridge MSE:", mean_squared_error(y_test, y_pred_ridge))
print("Ridge R2:", r2_score(y_test, y_pred_ridge))

# Lasso
lasso = Lasso(alpha=0.1)
lasso.fit(X_train, y_train)

y_pred_lasso = lasso.predict(X_test)
print("Lasso MSE:", mean_squared_error(y_test, y_pred_lasso))
print("Lasso R2:", r2_score(y_test, y_pred_lasso))

# 2. Confronto sui coefficienti (effetto della regolarizzazione)
# Vedrai che Ridge riduce le magnitudini, mentre Lasso mette a zero alcune feature.

coef_df = pd.DataFrame({
    "feature": X_train.columns,
    "ridge_coef": ridge.coef_,
    "lasso_coef": lasso.coef_,
})
print("\nCoefficienti Ridge vs Lasso:")
print(coef_df)

# 3. Tuning di alpha con cross‑validation (opzionale)
from sklearn.linear_model import RidgeCV, LassoCV

ridge_cv = RidgeCV(alphas=[0.1, 1.0, 10.0])
ridge_cv.fit(X_train, y_train)
print("\nMiglior alpha Ridge:", ridge_cv.alpha_)

lasso_cv = LassoCV(alphas=[0.001, 0.01, 0.1, 1.0], cv=5)
lasso_cv.fit(X_train, y_train)
print("\nMiglior alpha Lasso:", lasso_cv.alpha_)
