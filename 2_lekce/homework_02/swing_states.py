import requests
import pandas as pd
import numpy as np

with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/1976-2020-president.csv") as r:
  open("1976-2020-president.csv", 'w', encoding="utf-8").write(r.text)

president_elections_df = pd.read_csv("1976-2020-president.csv")

desired_width = 1000
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',100)

#print(president_elections_df.head())

# 1. Urči pořadí jednotlivých kandidátů v jednotlivých státech a v jednotlivých letech (pomocí metody rank()).
# Nezapomeň, že data je před použitím metody nutné seřadit a spolu s metodou rank() je nutné použít metodu
# groupby().

president_elections_df["Rank"] = president_elections_df.groupby(["state", "year"])["candidatevotes"]\
  .rank(method="max", ascending=False)

# 2. Pro další analýzu jsou důležití pouze vítězové. Ponech si v tabulce pouze řádky, které obsahují vítěze
# voleb v jednotlivých letech v jednotlivých státech.

president_elections_winners = president_elections_df[president_elections_df["Rank"] == 1]
#print(president_elections_winners)

# 3. Pomocí metody shift() přidej nový sloupec, abys v jednotlivých řádcích měl(a) po sobě vítězné strany ve
# dvou po sobě jdoucích letech.

president_elections_winners_sorted = president_elections_winners.sort_values(["state", "year"])
president_elections_winners_sorted["Rank_previous_year"] = president_elections_winners_sorted\
  .groupby(["state"])["party_simplified"].shift()
print(president_elections_winners_sorted)

president_elections_winners_sorted=president_elections_winners_sorted.dropna(axis = 0, \
                                                        subset=["Rank_previous_year"])
#axis 0 označuje řádky, axis 1 označuje sloupce

president_elections_winners_sorted["Swing"] = np.where(president_elections_winners_sorted["party_simplified"] == \
  president_elections_winners_sorted["Rank_previous_year"], 0, 1)
# 0 bude, když jsou hodnoty stejné, 1 když se liší
president_elections_winners_sorted = president_elections_winners_sorted.groupby(["state"])["Swing"].sum()

# 5. Proveď agregaci podle názvu státu a seřaď státy podle počtu změn vítězných stran.
president_elections_winners_sorted = pd.DataFrame(president_elections_winners_sorted)
president_elections_winners_sorted = president_elections_winners_sorted.sort_values("Swing")
print(president_elections_winners_sorted)

swing_states = president_elections_winners_sorted[president_elections_winners_sorted["Swing"] > 3]
print(f"Swing států je dohromady {swing_states.shape[0]}.")