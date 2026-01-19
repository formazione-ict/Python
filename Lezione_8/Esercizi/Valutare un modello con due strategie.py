# 📦 Importa le librerie
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score

# 📊 Dataset sintetico: [feature1, feature2]
X = np.array([
    [1, 2], [2, 1], [2, 2], [3, 3], [3, 2],
    [6, 7], [7, 6], [8, 8], [7, 7], [9, 6]
])
y = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])  # 0 = classe A, 1 = classe B

# 🧠 Modello
model = LogisticRegression()

# 🔹 Metodo 1: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
acc_split = accuracy_score(y_test, y_pred)
print(f"Train-Test Accuracy: {acc_split:.2f}")

# 🔸 Metodo 2: K-Fold Cross-Validation
scores = cross_val_score(model, X, y, cv=5)
print(f"K-Fold Accuracy (media): {scores.mean():.2f}")
print(f"K-Fold Std Dev: {scores.std():.2f}")