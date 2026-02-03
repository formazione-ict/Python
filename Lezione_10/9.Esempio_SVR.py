import pandas as pd

from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score

# 1. Carica dataset
diabetes = load_diabetes(as_frame=True)
X = diabetes.data        # 10 feature numeriche
y = diabetes.target      # progressione malattia (continuo)

# 2. Train/Test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Pipeline: StandardScaler + SVR (kernel RBF)
svr_rbf = make_pipeline(
    StandardScaler(),
    SVR(kernel="rbf", C=10.0, epsilon=0.1)
)
svr_rbf.fit(X_train, y_train)

# 4. Predizione e metriche
y_pred = svr_rbf.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
r2 = r2_score(y_test, y_pred)

print(f"SVR (RBF) MSE : {mse:.2f}")
print(f"SVR (RBF) RMSE: {rmse:.2f}")
print(f"SVR (RBF) R²  : {r2:.3f}")
