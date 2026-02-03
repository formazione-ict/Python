import lightgbm as lgb
import pandas as pd

from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# 1. Carica dataset
diabetes = load_diabetes(as_frame=True)  # X,y come DataFrame/Series [web:368]
X = diabetes.data
y = diabetes.target

# 2. Train/Test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Modello LightGBM Regressor (API compatibile sklearn)
model = lgb.LGBMRegressor(
    objective="regression",   # perdita quadratica per default [web:487]
    n_estimators=500,         # numero di alberi (boosting rounds)
    learning_rate=0.05,       # shrinkage
    max_depth=-1,             # -1 = nessun limite fisso, usa depth automatica
    num_leaves=31,            # complessità degli alberi
    subsample=0.8,            # frazione di righe per ogni albero
    colsample_bytree=0.8,     # frazione di feature per albero
    random_state=42
)

model.fit(X_train, y_train)

# 4. Predizione e metriche
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
r2 = r2_score(y_test, y_pred)

print(f"LightGBM MSE : {mse:.2f}")
print(f"LightGBM RMSE: {rmse:.2f}")
print(f"LightGBM R²  : {r2:.3f}")

# 5. (Opzionale) Importanza delle feature
feat_imp = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)
print("\nImportanza feature LightGBM:")
print(feat_imp)
