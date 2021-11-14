import statistics
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/crypto_prices.csv")
open("crypto_prices.csv", "wb").write(r.content)

df = pd.read_csv("crypto_prices.csv")

# zobrazení všech sloupců
desired_width = 1000
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',100)

#print(df.head())

# 1. Použij zavírací cenu kryptoměny (sloupec Close) a vypočti procentuální změnu jednotlivých kryptoměn.
# Pozor na to, ať se ti nepočítají ceny mezi jednotlivými měnami. Ošetřit to můžeš pomocí metody groupby(),
# jako jsme to dělali např. u metody shift().

# tzn. využiji korelaci
df["Change"] = df.groupby("Name")["Close"].pct_change()
# pivot - transformuje tabulku, aby byly vedle sebe řádky jednotlivých měn
df = df.pivot(index = "Date", columns = "Name", values="Change")
print(df.head())

# 2. Vytvoř korelační matici změn cen jednotlivých kryptoměn a zobraz je jako tabulku.
korelace = df.corr()
#print(korelace)

# 3. V tabulce vyber dvojici kryptoměn s vysokou hodnotou koeficientu korelace a jinou dvojici
# s koeficientem korelace blízko 0. Změny cen pro dvojice měn, které jsou hodně a naopak málo korelované,
# si zobraz jako bodový graf.
# vysoká hodnota korelace: Wrapped Bitcoin a Bitcoin
vysoka_korelace = df[["Wrapped Bitcoin", "Bitcoin"]]
seaborn.jointplot("Wrapped Bitcoin", "Bitcoin", vysoka_korelace, kind="scatter")
#plt.show()

# nízká hodnota korelace: Dogecoin a Aave
nizka_korelace = df[["Dogecoin", "Aave"]]
seaborn.jointplot("Dogecoin", "Aave", nizka_korelace, kind="scatter")
plt.show()