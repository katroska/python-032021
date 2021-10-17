import requests
import pandas
r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/data_with_ids.csv")
open("data_with_ids.csv", 'wb').write(r.content)

data_with_ids = pandas.read_csv("data_with_ids.csv")
print(data_with_ids.shape[0]) # vypíše jen počet řádků
print(data_with_ids["bank_id"].nunique()) # vypíše všechny řádky s unikátní číselnou hodnotou bank_id
data_with_ids_unique = data_with_ids.drop_duplicates(ignore_index=True) # co to dělá???
data_with_ids_unique.head()

