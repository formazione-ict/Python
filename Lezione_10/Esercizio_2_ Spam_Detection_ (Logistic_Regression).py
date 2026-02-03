from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Step 1: Carica dati (esempio)
emails = ['Buy now!', 'Meeting tomorrow', 'Win prize!', 'Hi, how are you?']
labels = [1, 0, 1, 0]   # 1=spam, 0=ham

# Step 2: TF-IDF Vectorization
vectorizer = TfidfVectorizer(max_features=1000)
X = vectorizer.fit_transform(emails)   # matrice sparsa

# Step 3: Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, labels, test_size=0.2, random_state=42
)

# Step 4: Logistic Regression
log_reg = LogisticRegression(max_iter=1000)
log_reg.fit(X_train, y_train)

# Step 5: Valuta
y_pred = log_reg.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy (Logistic Regression): {accuracy:.3f}')
print('\nClassification report:')
print(classification_report(y_test, y_pred))
