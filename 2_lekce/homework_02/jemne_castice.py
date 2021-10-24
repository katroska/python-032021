import requests
import pandas as pd
import numpy as np

with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/air_polution_ukol.csv") as r:
  open("air_polution_ukol.csv", 'w', encoding="utf-8").write(r.text)

# 1. Načti dataset a převeď sloupec date (datum měření) na typ datetime.
air_polution_df = pd.read_csv("air_polution_ukol.csv")

air_polution_df["date_converted"] = pd.to_datetime(air_polution_df["date"])
#print(air_polution_df.head())

# 2. Přidej sloupce s rokem a číslem měsíce, které získáš z data měření.
air_polution_df["year"] = air_polution_df["date_converted"].dt.year
air_polution_df["month"] = air_polution_df["date_converted"].dt.month
print(air_polution_df.head())

# 3. Vytvoř pivot tabulku s průměrným počtem množství jemných částic (sloupec pm25) v jednotlivých
# měsících a jednotlivých letech. Jako funkci pro agregaci můžeš použít numpy.mean.

air_polution_pivot = pd.pivot_table(air_polution_df, values="pm25", index="year", columns="month",
                                    aggfunc=np.mean, margins=True)
print(air_polution_pivot)