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

# 1. Poslední sloupec a poslední řádek obsahují nulové hodnoty. Zbav se tohoto sloupce a řádku.

lexikon_zvirat = lexikon_zvirat.dropna(how = "all", axis="rows")
lexikon_zvirat = lexikon_zvirat.dropna(how = "all", axis="columns")

# 2. Nastav sloupec id jako index pomocí metody set_index.

lexikon_zvirat = lexikon_zvirat.set_index("id")

#print(lexikon_zvirat.tail())

# Napiš funkci check_url, která bude mít jeden parametr radek. Funkce zkontroluje, jestli je odkaz
# v pořádku podle několika pravidel. K odkazu přistoupíš v těle funkce přes tečkovou notaci:
# radek.image_src.
# Zvol si jeden ze způsobů procházení tabulky, a na každý řádek zavolej funkci check_url. Pro každý řádek
# s neplatným odkazem vypiš název zvířete (title).


def check_url(radek):
  retezec = isinstance(radek.image_src, str)
  if retezec != True:
    print(radek.title)
    return
  zacatek = radek.image_src.startswith("https://zoopraha.cz/images/")
  konec = radek.image_src.lower().endswith("jpg")
  if zacatek != True:
    print(radek.title)
  elif konec != True:
    print(radek.title)

for radek in lexikon_zvirat.itertuples():
   check_url(radek)