# Obiettivo: classificare email spam (1) / ham (0) con Naive Bayes + TF‑IDF

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Step 1: Carica dati (esempio toy)
emails = [
    "Buy now! Limited offer!",
    "Meeting tomorrow at 10",
    "Win prize! Click here!",
    "Ciao, ci vediamo stasera?",
    "Free money!!! Claim your reward",
    "Ricordati della riunione di domani",
]
labels = [1, 0, 1, 0, 1, 0]   # 1 = spam, 0 = ham

# Step 2: TF-IDF Vectorization
vectorizer = TfidfVectorizer(max_features=1000)
X = vectorizer.fit_transform(emails)   # matrice sparsa (n_email, n_parole)

# Step 3: Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, labels, test_size=0.2, random_state=42
)

# Step 4: Naive Bayes
nb = MultinomialNB()
nb.fit(X_train, y_train)

# Step 5: Valuta
y_pred = nb.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.3f}")
print("\nClassification report:")
print(classification_report(y_test, y_pred))
