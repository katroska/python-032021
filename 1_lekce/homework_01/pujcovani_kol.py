import pandas
import requests
import pandas as pd
import numpy as np

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/london_merged.csv")
open("london_merged.csv", 'wb').write(r.content)

pujceni = pd.read_csv("london_merged.csv")
#print(pujceni.head())

# zobrazení všech sloupců
desired_width = 1000
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',100)

# 1. Vytvoř sloupec, do kterého z časové značky (sloupec timestamp) ulož rok.
#print(pujceni.dtypes)
pujceni["timestamp"] = pandas.to_datetime(pujceni["timestamp"], format= "%Y-%m-%d %H:%M:%S")

pujceni["year"] = pujceni["timestamp"].dt.year
print(pujceni)

# 2. Vytvoř kontingenční tabulku, která porovná kód počasí (sloupec weather_code) se sloupcem udávající rok.
# sloupec cnt je počet výpůjček

pujceni_pivot = pd.pivot_table(pujceni, index="weather_code", columns="year", values="cnt", aggfunc=np.sum, margins=True)

# 1 = Clear ; mostly clear but have some values with haze/fog/patches of fog/ fog in vicinity
# 2 = scattered clouds / few clouds
# 3 = Broken clouds
# 4 = Cloudy
# 7 = Rain/ light Rain shower/ Light rain
# 10 = rain with thunderstorm
# 26 = snowfall
# 94 = Freezing Fog

pujceni_pivot_df = pd.DataFrame(pujceni_pivot, index=None).reset_index(drop = False)
print(pujceni_pivot)

print(pujceni_pivot_df)