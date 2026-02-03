import xgboost as xgb
import pandas as pd

from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# 1. Carica dataset
diabetes = load_diabetes(as_frame=True)
X = diabetes.data        # 10 feature numeriche
y = diabetes.target      # target continuo

# 2. Train/Test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Modello XGBoost Regressor
xgb_reg = xgb.XGBRegressor(
    objective="reg:squarederror",  # loss per regressione [web:466][web:463]
    n_estimators=200,              # numero di alberi
    learning_rate=0.05,            # passo di apprendimento
    max_depth=4,                   # profondità massima degli alberi
    subsample=0.8,                 # frazione di righe per ogni albero
    colsample_bytree=0.8,          # frazione di colonne per ogni albero
    random_state=42
)

xgb_reg.fit(X_train, y_train)

# 4. Predizione e metriche
y_pred = xgb_reg.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
r2 = r2_score(y_test, y_pred)

print(f"XGBoost MSE : {mse:.2f}")
print(f"XGBoost RMSE: {rmse:.2f}")
print(f"XGBoost R²  : {r2:.3f}")
