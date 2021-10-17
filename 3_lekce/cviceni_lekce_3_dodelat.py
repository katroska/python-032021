import requests
import pandas

#r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/adopce-zvirat.csv")
#open("adopce-zvirat.csv", "wb").write(r.content)

adopce_df = pandas.read_csv("adopce-zvirat.csv", sep=";")
# sep je zkratka separator - primárně je to , my máme ;

adopce_df = adopce_df.dropna(how='all', axis='columns')
adopce_df = adopce_df.dropna(how='all', axis='rows')
print(adopce_df.head())

#když chci zobrazit všechny sloupce použiji těchto pár řádků
desired_width = 1000
pandas.set_option('display.width', desired_width)
pandas.set_option('display.max_columns',100)
print(adopce_df.head())

#jelikož je slovo blue i na začátku názvu, je "B" velké - to dělá potíže... můžu je převést na malé písmeno
#adopce_df["nazev_en"] = adopce_df["nazev_en"].str.lower()


#for zvire in adopce_df.itertuples():
# zvire_pro_adopci = zvire[zvire["nazev_en"]].include("blue")

#print(zvire_pro_adopci)