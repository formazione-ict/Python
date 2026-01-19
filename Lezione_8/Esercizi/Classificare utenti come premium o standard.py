# 📦 Importa le librerie
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# 📊 Dataset sintetico: [acquisti, tempo medio, recensioni]
X = np.array([
    [5, 120, 2],   # standard
    [20, 300, 10], # premium
    [3, 80, 0],    # standard
    [25, 400, 12], # premium
    [4, 100, 1],   # standard
    [18, 250, 8],  # premium
])

y = np.array([0, 1, 0, 1, 0, 1])  # 0 = standard, 1 = premium

# 🌳 Modello Decision Tree (tendente all’overfitting)
tree = DecisionTreeClassifier(max_depth=5, min_samples_split=2)
tree.fit(X, y)
y_pred_tree = tree.predict(X)

# 🌲 Modello Random Forest (più robusto)
forest = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
forest.fit(X, y)
y_pred_forest = forest.predict(X)

# 📈 Valutazione
print("🔍 Decision Tree")
print("Accuracy:", accuracy_score(y, y_pred_tree))
print(classification_report(y, y_pred_tree))

print("\n🔍 Random Forest")
print("Accuracy:", accuracy_score(y, y_pred_forest))
print(classification_report(y, y_pred_forest))