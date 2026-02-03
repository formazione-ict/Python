# Obiettivo: classificare il tipo/qualità di vino a partire da caratteristiche chimiche

import pandas as pd

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# Step 1: Carica dataset
wine = load_wine()
X, y = wine.data, wine.target   # X: features, y: classi (0,1,2)

print("Feature names:", wine.feature_names)
print("Classi:", wine.target_names)

# (opzionale) DataFrame per ispezionare rapidamente
df = pd.DataFrame(X, columns=wine.feature_names)
df["target"] = y
print(df.head())

# Step 2: Train/Test Split (stratificato sulle classi)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

# Step 3: Scaling (molto importante per SVM)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Step 4: SVM Multi-class (One-vs-One gestito internamente)
svm = SVC(kernel="rbf", C=10, gamma="scale")
svm.fit(X_train_scaled, y_train)

# Step 5: Valuta
y_pred = svm.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)

print(f"\nAccuracy SVM (wine): {accuracy:.3f}")
print("\nClassification report:")
print(classification_report(y_test, y_pred, target_names=wine.target_names))
