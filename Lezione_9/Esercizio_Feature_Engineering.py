import pandas as pd
import numpy as np

df = pd.read_csv("titanic.csv")
df.head()

# Gestione missing values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Fasce d'età
df["Age_group"] = pd.cut(df["Age"],
                         bins=[0, 12, 18, 35, 60, 100],
                         labels=["Child", "Teen", "YoungAdult", "Adult", "Senior"])
df[["Age", "Age_group"]].head(10)

# Dimensione familiare
df["Family_size"] = df["SibSp"] + df["Parch"] + 1
df[["SibSp", "Parch", "Family_size"]].head(10)

# Viaggia da solo?
df["Is_alone"] = (df["Family_size"] == 1).astype(int)
df[["Family_size", "Is_alone"]].head(10)

# Visualizzazione e analisi
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 4))
sns.countplot(x="Age_group", data=df)
plt.title("Distribuzione delle fasce d'età")
plt.show()

plt.figure(figsize=(8, 4))
sns.countplot(x="Family_size", data=df)
plt.title("Distribuzione della dimensione familiare")
plt.show()

sns.countplot(x="Is_alone", data=df)
plt.title("Viaggia da solo?")
plt.xticks([0, 1], ["No", "Sì"])
plt.show()