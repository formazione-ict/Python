import numpy as np
import pandas as pd

from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Carica dataset
diabetes = load_diabetes(as_frame=True)   # X,y come DataFrame/Series
X = diabetes.data      # 10 feature numeriche (age, bmi, bp, ...)
y = diabetes.target    # target continuo

print("Shape X:", X.shape)  # (442, 10)
print("Shape y:", y.shape)  # (442,)

# 2. Train/Test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Modello di regressione lineare
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)

# 4. Predizioni
y_pred = lin_reg.predict(X_test)

# 5. Valutazione (MSE e R^2)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:.2f}")
print(f"R^2 score: {r2:.3f}")

# 6. Coefficienti (interpretazione)
coeff_df = pd.DataFrame({
    "feature": X.columns,
    "coef": lin_reg.coef_
})
print("\nCoefficienti del modello:")
print(coeff_df)
