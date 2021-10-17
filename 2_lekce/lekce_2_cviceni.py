import requests
import pandas as pd
import numpy as np

#r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/baroko_half_marathon.csv")
#open("baroko_half_marathon.csv", 'wb').write(r.content)

baroko_half_marathon = pd.read_csv("baroko_half_marathon.csv")
print(baroko_half_marathon.head())

baroko_half_marathon = baroko_half_marathon.sort_values(["Jméno závodníka", "Ročník", "Rok závodu"])
print(baroko_half_marathon.head())

# chci si zobrazit jen ty sloupce, které mě zajímají:
#baroko_half_marathon = baroko_half_marathon[["Jméno závodníka", "Ročník", "Rok závodu", "FINISH"]]

# když si chci zobrazit všechny sloupce:
desired_width = 1000
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',100)


baroko_half_marathon["FINISH"] = pd.to_datetime(baroko_half_marathon["FINISH"]) # format="%H:%M:%S"
# když použiji formátovací řetězec, napíše se nám tam nějaké divné datum 01-01-1900
#baroko_half_marathon["REALTIME"] = pandas.to_datetime(baroko_half_marathon["REALTIME"])

baroko_half_marathon["FINISH_předchozí rok"] = baroko_half_marathon.groupby(["Jméno závodníka", "Ročník"])["FINISH"].shift()

baroko_half_marathon = baroko_half_marathon.dropna(subset=["FINISH_předchozí rok"]).reset_index(drop=True)

baroko_half_marathon["Rozdíl"] = baroko_half_marathon["FINISH"] - baroko_half_marathon["FINISH_předchozí rok"]
# kladná čísla jsou u těch, kdo se zlepšili, záporná  u těch, kdo se zhoršili

#baroko_half_marathon["Rozdíl"] = baroko_half_marathon["Rozdíl"].dt.total_seconds() # funguje taky (kdybych
# to chtěla převést na jednotlivé hodiny, minuty, sekundy, musela bych použít celočíselné dělení :)

# chci spočítat, kolik jich je lepších, horších
baroko_half_marathon["Rozdíl_text"] = np.where(baroko_half_marathon["Rozdíl"] > pd.Timedelta("0 days"), "zhoršení", "zlepšení")

# dvě varianty:
print(baroko_half_marathon.groupby(["Rozdíl_text"]).size())
print(baroko_half_marathon["Rozdíl_text"].value_counts())