import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report

# 1. Caricamento dati
url = "https://www.social-campus.com/files/titanic_2.csv"
df = pd.read_csv(url)

# 2. Preprocessing minimo

# Encoding Sex (0 = male, 1 = female)
df["Sex_encoded"] = df["Sex"].map({"male": 0, "female": 1})

# Gestione NaN nelle colonne numeriche che useremo
cols_num = ["Age", "Fare", "Pclass", "SibSp", "Parch"]
for c in cols_num:
    df[c] = df[c].fillna(df[c].median())

feature_cols = ["Age", "Fare", "Pclass", "Sex_encoded", "SibSp", "Parch"]

# Rimuovo eventuali righe ancora con NaN sulle feature o sul target
df = df.dropna(subset=feature_cols + ["Survived"])

X = df[feature_cols]
y = df["Survived"]

# 3. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# (Opzionale) 4. Scaling
# GaussianNB non richiede per forza lo scaling, ma per coerenza con gli altri esempi puoi farlo
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 5. Modello Gaussian Naive Bayes
gnb = GaussianNB()
gnb.fit(X_train_scaled, y_train)

# 6. Valutazione
y_pred = gnb.predict(X_test_scaled)
print(classification_report(y_test, y_pred))
