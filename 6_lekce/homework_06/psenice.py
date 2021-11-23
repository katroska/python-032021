import pandas as pd
import requests
from scipy.stats import mannwhitneyu

with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/psenice.csv") as r:
  open("psenice.csv", 'w', encoding="utf-8").write(r.text)

data = pd.read_csv("psenice.csv")
# print(data)

# H0: Délky zrn pšenice obou odrůd jsou stejné.
# H1: Délky zrn pšenice dvou odrůd se liší.

x = data["Rosa"]
y = data["Canadian"]
print(x.shape)
print(y.shape)
print(mannwhitneyu(x, y))

# Nulovou hypotézu na základě p-hodnoty zamítáme.
# P-hodnota (1.76e-24) je nižší než hladina významnosti 5 %.