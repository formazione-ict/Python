import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Caricamento del dataset Titanic dal sito
url = "https://www.social-campus.com/files/titanic_2.csv"
df = pd.read_csv(url)

# Encoding Sex
df["Sex_encoded"] = df["Sex"].map({"male": 0, "female": 1})

# Gestione NaN sulle numeriche usate (NO inplace sullo slice)
cols_num = ["Age", "Fare", "Pclass", "SibSp", "Parch"]
for c in cols_num:
    df[c] = df[c].fillna(df[c].median())

# Rimuovo eventuali righe ancora con NaN sulle feature o sul target
feature_cols = ["Age", "Fare", "Pclass", "Sex_encoded", "SibSp", "Parch"]
df = df.dropna(subset=feature_cols + ["Survived"])

# (debug) controlla che non ci siano più NaN
print("NaN per colonna dopo il cleaning:")
print(df[feature_cols].isna().sum())

X = df[feature_cols]
y = df["Survived"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)

# Probabilità solo del primo campione del test set
# y_proba = model.predict_proba(X_test_scaled)[:, 1]  # Prendi la probabilità di sopravvivenza (colonna 1)
proba_first = model.predict_proba(X_test_scaled[:1])  # Prendi solo il primo campione
print("Probabilità primo campione (classe 0, classe 1):", proba_first)
print("Probabilità sopravvivenza primo campione:", proba_first[0, 1])

y_pred = model.predict(X_test_scaled)
print(classification_report(y_test, y_pred))

