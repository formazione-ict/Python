# 📦 Importa le librerie
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 📊 Dataset sintetico: [parole sospette, link, lunghezza]
X = np.array([
    [3, 2, 120],   # spam
    [0, 0, 300],   # non spam
    [2, 1, 150],   # spam
    [0, 0, 250],   # non spam
    [4, 3, 100],   # spam
    [1, 0, 200],   # non spam
])

# 🎯 Etichette: 1 = spam, 0 = non spam
y = np.array([1, 0, 1, 0, 1, 0])

# 🧠 Crea e allena il modello
model = LogisticRegression()
model.fit(X, y)

# 🔮 Previsioni
y_pred = model.predict(X)
y_prob = model.predict_proba(X)

# 📈 Valutazione
print("Accuracy:", accuracy_score(y, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y, y_pred))
print("Classification Report:\n", classification_report(y, y_pred))

# 🔍 Visualizza probabilità per ogni esempio
for i, prob in enumerate(y_prob):
    print(f"Messaggio {i+1}: Probabilità spam = {prob[1]:.2f}, Classe predetta = {y_pred[i]}")