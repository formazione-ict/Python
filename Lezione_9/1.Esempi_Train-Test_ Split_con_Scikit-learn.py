# Importa il modulo che contiene i dataset di esempio.
from sklearn import datasets

# Esempio Iris - Classificazione (150 fiori, 3 specie)
iris = datasets.load_iris()
X_iris, y_iris = iris.data, iris.target 	# le feature (misure) e le etichette (specie)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X_iris, y_iris,			# X = feature (input), y = etichette (target)
    test_size=0.2,          # 80% train, 20% test
    random_state=42,        # reproducibilità, stessa divisione ogni volta
    stratify=y_iris         # mantiene le proporzioni delle classi, se è classificazione, mantiene nel train/test la stessa distribuzione di classi (es. 30% classe 1, 70% classe 0)
)

# Stampa quanti campioni sono finiti nel train e quanti nel test
print(f'Iris - Train: {X_train.shape[0]}, Test: {X_test.shape[0]}')


# Esempio Wine - Classificazione (178 vini, 3 classi)
wine = datasets.load_wine()
X_wine, y_wine = wine.data, wine.target  # le feature (misure) e le etichette (classi)

X_train_wine, X_test_wine, y_train_wine, y_test_wine = train_test_split(
    X_wine, y_wine,          # X = feature (input), y = etichette (target)
    test_size=0.3,           # 70% train, 30% test 
    random_state=50,         # reproducibilità, stessa divisione ogni volta 
    stratify=y_wine          # mantiene le proporzioni delle classi
)

# Stampa quanti campioni sono finiti nel train e quanti nel test per Wine
print(f'Wine - Train: {X_train_wine.shape[0]}, Test: {X_test_wine.shape[0]}')

# Esempio Digits - Riconoscimento numeri (1797 immagini 8x8 di cifre scritte a mano)
digits = datasets.load_digits()
X_digits, y_digits = digits.data, digits.target  # le feature (pixel) e le etichette (numeri)

X_train_digits, X_test_digits, y_train_digits, y_test_digits = train_test_split(
    X_digits, y_digits,      # X = feature (input), y = etichette (target)
    test_size=0.15,          # 85% train, % test
    random_state=32,         # reproducibilità, stessa divisione ogni volta
    stratify=y_digits        # mantiene le proporzioni delle classi 
)

# Stampa quanti campioni sono finiti nel train e quanti nel test per Digits
print(f'Digits - Train: {X_train_digits.shape[0]}, Test: {X_test_digits.shape[0]}')
