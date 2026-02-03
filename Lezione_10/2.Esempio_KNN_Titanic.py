import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

url = "https://www.social-campus.com/files/titanic_2.csv"
df = pd.read_csv(url)

# Encoding Sex
df["Sex_encoded"] = df["Sex"].map({"male": 0, "female": 1})

# Colonne numeriche che usiamo
cols_num = ["Age", "Fare", "Pclass", "SibSp", "Parch"]
for c in cols_num:
    df[c] = df[c].fillna(df[c].median())

feature_cols = ["Age", "Fare", "Pclass", "Sex_encoded", "SibSp", "Parch"]
df = df.dropna(subset=feature_cols + ["Survived"])

X = df[feature_cols]
y = df["Survived"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# KNN è sensibile alla scala → standardizziamo
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Modello KNN con k variabile. Si vede come cambiano precision/recall al variare di k (concetto di bias–variance)
for k in [1, 3, 5, 11, 21]:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train_scaled, y_train)
    y_pred = knn.predict(X_test_scaled)
    print(f"\n=== k = {k} ===")
    print(classification_report(y_test, y_pred))


y_pred = knn.predict(X_test_scaled)
print(classification_report(y_test, y_pred))
