import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Step 1: Carica dati (esempio sintetico)
df = pd.DataFrame({
    "Area": [1500, 2000, 1200, 1800, 2500],
    "Bedrooms": [3, 4, 2, 3, 5],
    "Age": [10, 5, 20, 8, 2],
    "Distance": [5, 3, 8, 4, 2],                        # km dal centro città
    "Price": [300000, 400000, 250000, 350000, 500000]
})

print(df)

# Step 2: Separa feature e target
X = df[["Area", "Bedrooms", "Age", "Distance"]]
y = df["Price"]

# Step 3: Train/Test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.4, random_state=42                # (con solo 5 righe, uso 60% train / 40% test per avere almeno 2 campioni di test)
)

# Step 4: Modello di regressione lineare
model = LinearRegression()
model.fit(X_train, y_train)

# Step 5: Predizione sul test set
y_pred = model.predict(X_test)

print("\nValori reali:", list(y_test))
print("Valori predetti:", list(y_pred))

# Step 6: Metriche di regressione
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\nMSE : {mse:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"MAE : {mae:.2f}")
print(f"R²  : {r2:.3f}")
