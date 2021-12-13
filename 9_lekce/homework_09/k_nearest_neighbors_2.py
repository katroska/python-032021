import requests
import pandas as pd
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix, precision_score, f1_score, accuracy_score

import matplotlib.pyplot as plt

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/kosatce.csv")
open("kosatce.csv", "wb").write(r.content)

# Příprava dat:
data = pd.read_csv("kosatce.csv")
# print(data.shape)
data = data.dropna()
# print(data.shape)
print(data.head())

# Rozdělení vstupních proměnných a cílové hodnoty:
vstup = X = data.drop(columns=["target"])
vystup = y = data["target"]

# Rozdělení dat na trénovací a testovací sadu:
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# print(X_train.shape, y_train.shape)
# print(X_test.shape, y_test.shape)

# Normalizace dat:
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Trénování dat:
clf = KNeighborsClassifier()
clf.fit(X_train, y_train)

# Vyhodnocení modelu:
y_pred = clf.predict(X_test)
# print(y_pred)

print(confusion_matrix(y_true=y_test, y_pred=y_pred))
# graf confusion matrix
# ConfusionMatrixDisplay.from_estimator(clf, X_test, y_test, display_labels=clf.classes_, cmap=plt.cm.Blues)
# plt.show()

# Upravení parametrů modelu
ks = [1, 3, 5, 7, 9, 11, 13, 15, 16, 17, 19, 21, 23, 25, 27, 29]
f1_scores = []

for k in ks:
    clf = KNeighborsClassifier(n_neighbors=k)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    f1_scores.append(f1_score(y_test, y_pred))

# plt.plot(ks, f1_scores)
# plt.show()

# 7. Zaverecna predikce
clf = KNeighborsClassifier(n_neighbors=13)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print(f1_score(y_test, y_pred))

# metrika f1_score dosáhne alespoň 85 % při hodnotách k náležící do intervalu <1, 12> a <14,17> a 21 a 25
# Pro některé hodnoty k je možné předpovědět typ kosatce na základě těchto dat tak, aby metrika f1_score
# dosáhla alespoň 85 %, ale celkově to neplatí.

