import requests
import pandas

# data o výpadcích televizního signálu
# napíše informaci, jestli signál vypadl, nebo se obnovil

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/signal_monitoring.csv")
open("signal_monitoring.csv", 'wb').write(r.content)

signal_monitoring = pandas.read_csv("singal_monitoring.csv")

#vytvořím si nový sloupec
#signal_monitoring["event_date_time_2"] = signal_monitoring["event_date_time"].shift()
print(signal_monitoring.head())

singal_monitoring["event_date_time"] = pandas.to_datetime(singal_monigoring["event_date_time"])

#shift posune hodnoty ve sloupci event_date_time_2 o jeden řádek dolů, takže když dám k závorkám do
# shift -1, posunu nahoru
signal_monitoring["event_date_time_2"] = signal_monitoring["event_date_time"].shift(-1)

# chci odečíst ty dvě hodnoty od sebe, takže přidám nový sloupec a odečtu je
signal_monitoring["event_lenght"] = signal_monitoring["event_date_time_2"] - signal_monitoring["event_date_time"]

# chci vymazat řádky se záznamem, kde je napsáno, jak dlouho je signál aktivní, chci si nechat jen ty, kde je tan výpadek??
## chybí