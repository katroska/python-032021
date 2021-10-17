import requests
import pandas

with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/air_polution_ukol.csv") as r:
  open("air_polution_ukol.csv", 'w', encoding="utf-8").write(r.text)

df_air_polution = pandas.read_csv("air_polution_ukol.csv")

print(df_air_polution.head())