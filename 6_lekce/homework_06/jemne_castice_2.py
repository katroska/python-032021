import pandas as pd
import requests
from scipy.stats import mannwhitneyu

with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/air_polution_ukol.csv") as r:
  open("air_polution_ukol.csv", 'w', encoding="utf-8").write(r.text)

data = pd.read_csv("air_polution_ukol.csv")

data = data.dropna(how='all', axis='columns')
data = data.dropna(how='all', axis='rows')

data["date_converted"] = pd.to_datetime(data["date"])

data["year"] = data["date_converted"].dt.year
data["month"] = data["date_converted"].dt.month

# x = data[((data["year"] == 2019) | (data["year"] == 2020)) & (data["month"] == 1)]

# H0: Průměrné množství jemných částic ve vzduchu jsou v obou měsících stejné.
# H1: Průměrné množství jemných částic ve vzduchu jsou v roce 2019 jiné (nižší) než v roce 2020.

x = data[(data["year"] == 2019) & (data["month"] == 1)]["pm25"]
y = data[(data["year"] == 2020) & (data["month"] == 1)]["pm25"]
print(x.shape)
print(y.shape)
print(mannwhitneyu(x, y))

# Když vyjde p-hodnota testu 1.1 %, nulovou hypotézu na hladině významnosti 5 % bych zamítla.
# (Pokud by p-hodnota testu byla vyšší než 5 %, nulovou hypotézu bych nezamítla.)