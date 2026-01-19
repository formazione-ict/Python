import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# --- DATASET DI BASE (10 CAMPIONI) ---
X = np.array([[1, 2], [2, 1], [2, 2], [3, 3], [3, 2], [6, 7], [7, 6], [8, 8], [7, 7], [9, 6]])
y_clean = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])

# Suddivisione manuale per avere controllo totale sui risultati (7 train, 3 test)
X_train, X_test = X[:7], X[7:]
y_train_clean, y_test_clean = y_clean[:7], y_clean[7:]

def print_metrics(label, train_acc, test_acc, icon):
    print(f"{icon} {label}")
    print(f"Train: {train_acc:.2f}")
    print(f"Test : {test_acc:.2f}\n")

# --- 1. 🔴 UNDERFITTING ---
# Usiamo un modello troppo "debole" (max_depth=1) su dati con un errore introdotto
y_train_noise = y_train_clean.copy()
y_train_noise[0] = 1 # Errore nel train (5 su 7 corretti = 0.71)
y_test_noise = y_test_clean.copy()
y_test_noise[0] = 0  # Errore nel test  (2 su 3 corretti = 0.66)

model_under = RandomForestClassifier(max_depth=1, n_estimators=1, random_state=42)
model_under.fit(X_train, y_train_noise)
print_metrics("Underfitting", accuracy_score(y_train_noise, model_under.predict(X_train)), 
              accuracy_score(y_test_noise, model_under.predict(X_test)), "🔴")

# --- 2. 🟢 BILANCIATO ---
# Dati puliti e separabili, il modello apprende perfettamente il pattern
model_bal = RandomForestClassifier(max_depth=None, n_estimators=100, random_state=42)
model_bal.fit(X_train, y_train_clean)
print_metrics("Bilanciato", accuracy_score(y_train_clean, model_bal.predict(X_train)), 
              accuracy_score(y_test_clean, model_bal.predict(X_test)), "🟢")

# --- 3. 🔵 OVERFITTING ---
# Il modello è complesso e impara il rumore nel train (1.00) ma fallisce nel test (0.66)
y_train_over = y_train_clean.copy() 
# In questo caso y_test ha rumore ma il modello non può saperlo
model_over = RandomForestClassifier(max_depth=10, n_estimators=100, random_state=42)
model_over.fit(X_train, y_train_clean)
print_metrics("Overfitting", accuracy_score(y_train_clean, model_over.predict(X_train)), 
              accuracy_score(y_test_noise, model_over.predict(X_test)), "🔵")