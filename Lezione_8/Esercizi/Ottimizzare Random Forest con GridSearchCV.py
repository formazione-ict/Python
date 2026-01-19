# 📦 Importa le librerie
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import accuracy_score, classification_report

# 📊 Dataset sintetico: [feature1, feature2]
X = np.array([
    [1, 2], [2, 1], [2, 2], [3, 3], [3, 2],
    [6, 7], [7, 6], [8, 8], [7, 7], [9, 6]
])
y = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])  # 0 = classe A, 1 = classe B

# 🔀 Suddividi in train/test
# 'stratify=y' assicura che entrambe le classi siano presenti sia in train che in test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# Modello base (Supervised Classification)
model = RandomForestClassifier(random_state=42)

# Griglia di iperparametri
params = {
    'n_estimators': [50, 100],
    'max_depth': [3, 5]
}

# GridSearchCV con 2-fold cross-validation
# Ridotto cv=2 perché hai pochi campioni totali nel training set (7 campioni)
grid = GridSearchCV(model, params, cv=2)
grid.fit(X_train, y_train)

# Miglior modello trovato
best_model = grid.best_estimator_

# Valutazione sul test set
y_pred = best_model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred, zero_division=0))

# Parametri ottimali
print("Best Parameters:", grid.best_params_)