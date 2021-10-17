import requests
import pandas as pd
import numpy as np

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/titanic.csv")
open("titanic.csv", 'wb').write(r.content)

titanic = pd.read_csv("titanic.csv")
print(titanic.head())

titanic_pivot = pd.pivot_table(titanic, index="Sex", columns="Pclass", values="Survived", aggfunc=np.mean, margins=True)

print(titanic_pivot)