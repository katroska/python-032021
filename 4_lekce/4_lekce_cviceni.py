import requests
import pandas
import statistics

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/UberDrives.csv")
open("UberDrives.csv", "wb").write(r.content)

uber = pandas.read_csv("UberDrives.csv")
print(uber)

# na posledním řádku je napsaný nějaký součet, který by nám ovlivňoval výpočty... odstraníme ho
#uber_cista_data = uber.iloc[:-1]
#print(uber_cista_data)
# aktualizace: Jirka už řádek smazal, takže tohle už nemusím používat


# 1. Pro ujetou vzdálenost (sloupec MILES) urči průměr, medián, rozptyl a varianční rozpětí podle typu jízdy
# (sloupec CATEGORY)

# nejdřív musím data seskupit podle typu jízdy... všechny věci mám počítat pro každý typ zvlášť!

prumer = uber["MILES"].mean()
print(prumer)

median = uber["MILES"].median()
print(median)

rozptyl = statistics.pvariance(uber["MILES"])
print(rozptyl)

# varianční rozpětí = rozdíl nejvyšší a nejnižší hodnoty
variancni_rozpeti = max(uber["MILES"]) - min(uber["MILES"])
print(variancni_rozpeti)

# variační rozpětí podle typu jízdy... musím nejdřív udělat groupby podle typu jízdy!!!
# abych mohla počítat s hodnotami, musím si je převést na běžný dataframe (jinak je to tuple, se kterým
# nejdou provádět matematické operace)

# kategorie = uber.groupby(["CATEGORY"])
# print(kategorie)
#
# variacni_rozptyl_kategorie = max(uber.groupby(["CATEGORY"])) - min(uber.groupby(["CATEGORY"]))
# print(variacni_rozptyl_kategorie)

# když chci výpočty udělat najednou, můžu napsat víc aggregačních funkcí za sebe takto:
#
# uber = pandas.read_csv("UberDrives.csv")
# data_grouped = data.groupby(["CATEGORY"]).agg({"MILES": ["mean", "median", "var", "std", "count", "max", "min"]})
# data_grouped = pandas.DataFrame(data_grouped)
# data_grouped = data_grouped.reset_index()
# data_grouped["var_rozp"] = data_grouped.iloc[:, -2] - data_grouped.iloc[:, -1]
# print(data_grouped)


#2. Vypočti délku jízdy (rozdíl časových údajů ve sloupcích END_DATE a START_DATE) v minutách nebo hodinách.


# 3. Zjisti, jaká je korelace mezi délkou jízdy a vzdáleností.

# řešení od Jirky: úkol 2 a 3
# data["START_DATE"] = pandas.to_datetime(data["START_DATE"])
# data["END_DATE"] = pandas.to_datetime(data["END_DATE"])
# data["Duration"] = data["END_DATE"] - data["START_DATE"]
# data["Duration"] = data["Duration"].dt.seconds / 60  ... převedeno na minuty (sekundy děleno 60)
# print(data[["Duration", "MILES"]].corr())


# Letadlo
# import itertools
# numbers = list(range(1, 48))
# letters = ["A", "B", "C", "D", "E", "F"]
# places = list(itertools.product(numbers, letters))
# for item in places:
#     print(f"{item[0]}{item[1]}")
