import requests
import pandas

with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/1976-2020-president.csv") as r:
  open("1976-2020-president.csv", 'w', encoding="utf-8").write(r.text)

df_president = pandas.read_csv("1976-2020-president.csv")

print(df_president.head())