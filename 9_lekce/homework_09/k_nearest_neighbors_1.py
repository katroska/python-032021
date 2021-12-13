import requests
import pandas as pd
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix, precision_score, f1_score, accuracy_score

import matplotlib.pyplot as plt

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/water-potability.csv")
open("water-potability.csv", 'wb').write(r.content)

# 1. Definice problému
# Chceme určit, jestli je voda pitná nebo ne. Je pro nás důležité, abychom raději označili pitnou vodu za nepitnou,
# než nepitnou za pitnou. Raději nebudeme pít vůbec, než abychom se napili nepitné vody a onemocněli.

# 2. Příprava dat:
data = pd.read_csv("water-potability.csv")
# print(data.shape)
data = data.dropna()
# print(data.shape)

# Jak jsou cílové hodnoty rozdělené:
# print(data["Potability"].value_counts(normalize=True))

# Rozdělení vstupních proměnných a cílové hodnoty:
vstup = X = data.drop(columns=["Potability"])
vystup = y = data["Potability"]

# Rozdělení dat na trénovací a testovací sadu:
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# print(X_train.shape, y_train.shape)
# print(X_test.shape, y_test.shape)

# Normalizace dat:
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# print(X_train)

# 3. Výběr algoritmu: KNN = K Nearest Neighbors

# 4. Trénování dat:
clf = KNeighborsClassifier()
clf.fit(X_train, y_train)

# 5. Vyhodnocení modelu:
y_pred = clf.predict(X_test)
# print(y_pred)

print(confusion_matrix(y_true=y_test, y_pred=y_pred))

# ConfusionMatrixDisplay.from_estimator(clf, X_test, y_test, display_labels=clf.classes_, cmap=plt.cm.Blues)
# plt.show()

# Zjistíme, kolik hodnot jsme trefili správně (1.0 je 100 %):
print(74/(74 + 52))
print(precision_score(y_test, y_pred))

# 6. Upravení parametrů modelu
ks = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21] # hodnoty k nebližšího okolí
precision_scores = []
for k in ks:
    clf = KNeighborsClassifier(n_neighbors=k)  # model, classifier
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    precision_scores.append(precision_score(y_test, y_pred))
plt.plot(ks, precision_scores)
plt.show()

# nejlepšího výsledku jsem dosáhla pro k = 13

# 7. Zaverecna predikce
clf = KNeighborsClassifier(n_neighbors=13)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print(f1_score(y_test, y_pred))

# Na lekci (při použití f1_score) bylo nejlepšího výsledku dosaženo, když k = 3. Výsledky se tedy liší.

# Confusion matrix vypadá takto:
# [[179  52]
#  [ 98  74]]
# Výpočet, kterým dosáhneme stejného výsledku jako při použití precision_score() je zde:
# print(74/(74 + 52))