import pandas
import requests
import matplotlib.pyplot as plt

# stáhneme si soubor s plánem tržeb
r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/sales_plan.csv")
open("sales_plan.csv", 'wb').write(r.content)

# nahrajeme si stažený soubor do tabulky df_plan
df_plan = pandas.read_csv("sales_plan.csv")

# print(df_plan.head()) # začátek tabulky
# print(df_plan.tail())  #konec tabulky

# vytvořím kumulativní součet
# kumulativní součet by měl začínat vždy na začátku roku, začínáme od nuly
# přidám nový sloupeček s názvem cumsum

df_plan["sales_plan_cumsum"] = df_plan.groupby("year")["sales"].cumsum()

# vytvořila jsem agregaci, v závorce u groupby je název sloupečku, podle kterého se bude něco dít,
# "sales" je soupec, který se bude sčítat a cumsum je funcke kumulativního součtu

print(df_plan)

# REÁLNÉ PLATBY
# stáhneme soubor se skutečnými tržbami
r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/sales_actual.csv")
open("sales_actual.csv", 'wb').write(r.content)

df_actual = pandas.read_csv("sales_actual.csv")

# data si dám do skupin po měsících, abych mohla porovnat plán a realitu podle konkrétního měsíce
# datum ve sloupci "date" bere jako obyčejný text - musíme převést na datový typ datetime
df_actual["date"] = pandas.to_datetime(df_actual["date"])
df_actual["month"] = df_actual["date"].dt.month # tímhle získám z datumu jen číslo měsíce
df_actual["year"] = df_actual["date"].dt.year # tímhle získám z datumu jen číslo roku
print(df_actual.head())

# chci udělat součet dat po měsících a letech, chci sečíst kontrakty ze stejného měsíce a
# vytvořím si novou tabulku - pro jeden rok a měsíc bude obsahovat jen jednu buňku

df_actual_grouped = df_actual.groupby(["month", "year"]).sum()

# provedu kumulativní součet
df_actual_grouped["sales_actual_cumsum"] = df_actual_grouped["contract_value"].cumsum()

#chci se zbavit indexů - měsíc a rok jsou jako indexy, když je odstraním, stane se z nich...?
df_actual_grouped = df_actual_grouped.reset_index()

# vytvořím si novou tabulku, ve které ty dvě předchozí spojím

df_joined = pandas.merge(df_plan, df_actual_grouped, on=["month", "year"])
# když dám on = month, year - dá do jednoho řádku hodnoty ve stejném měsíci a roce
# u funkce "on=" na pořadí nezáleží

df_joined = df_joined.set_index("month")
# měsíc je teď hodnota, která je nejdůležitější

print(df_joined.tail())

"""
# UDĚLÁME GRAF
# bude zobrazovat dvě časové řady
ax = df_joined.plot(color="red", y="sales_plan_cumsum", title="Skutečné vs plánované tržby")
# color je barva čáry, y je co se na osu Y vyznačí, title je název grafu
# ax = je vlastně vytvoření plochy, prostor, do kterého vykresluji graf;
# používám ji proto, abych do ní mohla vložit ještě druhý graf

df_joined.plot(kind="bar", y="sales_actual_cumsum", ax=ax)
# kind - je druh grafu, bar je sloupcový graf
# tím ax = ax udělám to, že spojím ty dva grafy do jednoho

# df_joined.index = df_joined.index.astype(str)
#aby nebyla posunutá ta linie

df_joined.plot(kind="bar", y=["sales_plan_cumsum", "sales_actual_cumsum"])
# udělám z těch grafů dva sloupcové grafy (předtím byl jeden sloupcový a jeden jako čára)
plt.show()
"""

# KONTINGENČNÍ TABULKY
import numpy
df_actual_pivot = pandas.pivot_table(df_actual, index="country", columns="sales_manager", values="contract_value", aggfunc=numpy.sum, margins=True)
print(df_actual_pivot)
# margins = true dodá celkový součet tržeb za jednotlivé země (u všech obchodníků)