import requests
import pandas
import math

#r = requests.get()

sportoviste = pandas.read_json("sportoviste.json")

# čistění dat
sportoviste = sportoviste.dropna(how="all", axis="columns")
sportoviste = sportoviste.reset_index("OBJECTID")
print(sportoviste.head())

# přejmenujeme sloupce, protože GPS souřadnice jsou prohozené (místo Opavy odkazuje do Jemenu)
sportoviste = sportoviste.rename(columns={"POINT_Y": "zemepisna_sirka", "POINT_X": "zemepisna_delka"})

poloha_nadrazi_opava = {49.9345092, 17.9085369} # první je zeměpisná šířka a druhé je zeměpisná délka

# přidáme fci, kterou vytvořila Lída
def vzdalenost_od_bodu(radek, bod):
  #Vypocet vzdalenosti mezi dvema body (Eukleidovska vzdalenost)
  vzdalenost = math.sqrt((bod[0] - radek.zemepisna_sirka) ** 2 + (bod[1] - radek.zemepisna_delka) ** 2)
  vzdalenost_km = vzdalenost * (2.0 * 6378 * math.pi / 360.0)
  vzdalenost_km = round(vzdalenost_km, 2)
  return vzdalenost_km

# tato fce vezme jeden řádek a spočítá vzdálenost od jednoho bodu,
# jak to uděláme, abychom to využili ve více řádcích? metoda apply

sportoviste["vzdalenost_od_nadrazi_v_km"] = sportoviste.apply(vzdalenost_od_bodu, axis = 1, args = (poloha_nadrazi_opava))
#print() # doplnit