import requests
import pandas
import numpy

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/user_registration.json")
open("user_registration.json", 'wb').write(r.content)

df_user_registration = pandas.read_json("user_registration.json")

print(df_user_registration.columns)
print(df_user_registration.head())

# kumulativní součet
df_user_registration["date_time"] = pandas.to_datetime(df_user_registration["date_time"])
df_user_registration["day"] = df_user_registration["date_time"].dt.day
df_user_registration = df_user_registration.groupby(["day"]).size()
# nebo df_user_registration = df_user_registration.groupby(["day"])["ip_adress"].count()
# aby se sečetly jednotlivé řádky? moc nevím...
print(df_user_registration.cumsum())

# abychom se zbavili toho jednoho člověka, který je připočítán 


# kontingenční tabulka
#user_registration_pivot = pandas.pivot_table(df_user_registration, index="age_group", columns="marketing_channel", aggfunc=numpy.count_nonzero)
# aggfunc=numpy.count_nonzero vložit místo sumy
#print(user_registration_pivot)