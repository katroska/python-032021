import requests
import pandas

# chci porovnat index ekonomické svobody jednotlivých států a chci zjistit, jak se mění

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/ioef.csv")
open("ioef.csv", 'wb').write(r.content)

ioef = pandas.read_csv("ioef.csv")
print(ioef.head())


# chci se podívat na vývoj, využiji metodu shift

#ioef["Rank"] = ioef["Overall Score"].rank(ascending=False)
# chci to počítat od nejvyššího skóre, protože čím vyšší skóre, tím lepší
# je tam ale hodnota za více let, seskupím to podle jednotlivých let
ioef["Rank"] = ioef.groupby(["Index Year"])["Overall Score"].rank(ascending=False)

# abychom si mohli porovnat, jak si nějaká země vede rok po roku, musím si to seřadit jinak, použiji sort by
ioef = ioef.sort_values(["Name", "Index Year"])

ioef["Rank Previous Year"] = ioef.groupby(["Name"])["Rank"].shift()

ioef["Difference"] = ioef["Rank"] - ioef["Rank Previous Year"]
print(ioef.head())
