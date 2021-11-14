import requests
import pandas as pd
import numpy as np
from scipy.stats import gmean

#r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/crypto_prices.csv")
#open("crypto_prices.csv", "wb").write(r.content)

df = pd.read_csv("crypto_prices.csv")

# zobrazení všech sloupců
desired_width = 1000
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',100)

#print(df.head())
# vyfiltruji měnu "XMR"
df_XMR = df[df["Symbol"] == "XMR"]

# přidám sloupec Change se změnou ceny
df_XMR["Change"] = df_XMR.groupby("Name")["Close"].pct_change() + 1

print(round((gmean(df_XMR["Change"].dropna().tolist()) - 1), 10))