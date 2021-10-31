# ZADÁNÍ: https://github.com/pesikj/python-032021/blob/master/01_pandas/03/ukol/ukol.ipynb

import requests
import pandas as pd
import numpy as np

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/lexikon-zvirat.csv")
open("lexikon-zvirat.csv", "wb").write(r.content)
lexikon_zvirat = pd.read_csv("lexikon-zvirat.csv", sep=";")

desired_width = 1000
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',100)

# Chceme ke každému zvířeti vytvořit popisek na tabulku do zoo. Popisek bude využívat sloupců
# title (název zvířete), food (typ stravy), food_note (vysvětlující doplněk ke stravě) a description
# (jak zvíře poznáme). Napiš funkci popisek, která bude mít jeden parametr radek. Funkce spojí informace
# dohromady. Následně použijte metodu apply, abyste vytvořili nový sloupec s tímto popiskem.

def popisek(radek):
  return f"{radek.title} preferuje následující typ stravy: {radek.food}. Konkrétně ocení, když mu do misky" \
         f" přistanou: {radek.food_note}. {radek.description}"

lexikon_zvirat["popisek_na_tabuku"] = lexikon_zvirat.apply(popisek, axis=1)
print(lexikon_zvirat["popisek_na_tabuku"].iloc[300])