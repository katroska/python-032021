import pandas
import requests
import numpy
import datetime

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/invoices.csv")
open("invoices.csv", 'wb').write(r.content)

# soubor obsahuje informace o fakturách, nás bude zajímat sloupec invoice date

invoices = pandas.read_csv("invoices.csv")
print(invoices.head())

# jaké typy mají jednotlivé sloupce
#print(invoices.dtype??)
# object - pracuje s ním jako s řetězcem (stringem)
# takže řádek invoices_date budu chtít převést na typ: datum a čas


invoices["invoice_date_converted"] = pandas.to_datetime(invoices["invoice_date"], format="%d. %m. %Y")
# když tam není ten format, převedou se špatně dny a měsíce - v některých případech se to přehodí
print(invoices.head)

# délka lhůty bude 60 dnů, použiji Timedelta - uchovává informaci o počtu (a také o počtu čeho)
invoices["due_date"] = invoices["invoice_date_converted"] + pandas.Timedelta("60 days")
# nebo můžu použít tzv. iso normu, takže napíšu P60D, kde D je den a P je perioda (=duration),
# funguje to stejně jako to "60 days"
invoices["due_date"] = invoices["invoice_date_converted"] + pandas.Timedelta("P60D")

# chci se podívat, které platby jsou před splatností a které po ní
# porovnám dva datumy: due_date a dnešní datum - které si nastavím na 1.9.2021

#today_date = datetime.datetime(2021, 9, 1)
# pokud chci mít today_date stále aktuální (dynamické), nastavím tam datetime.datetime.now()
today_date = datetime.datetime.now()
invoices["status"] = numpy.where(invoices["due_date"] < today_date, "po splatnosti", "před splatností")
print(invoices.head())

# chci sdružit faktury, které jsou před splatností a po splatnosti do jedné části
print(invoices.groupby("status")["amount"].sum())


# INVOICES 2
# tentokrát budeme naopak timedelta počítat, ne vytvářet

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/invoices_2.csv")
open("invoices_2.csv", 'wb').write(r.content)
invoices_2 = pandas.read_csv("invoices_2.csv")
invoices_2["invoice_date"] = pandas.to_datetime(invoices_2["invoice_date"], format="%d. %m. %Y")
invoices_2["payment_date"] = pandas.to_datetime(invoices_2["payment_date"], format="%d. %m. %Y")
print(invoices_2.head())

# vytvořím si tabulku, nejdřív si do ní potřebuju uložit jen ty zaplacené a s těmi pracovat
# vím, že ty, které jsou zaplacené, mají ve sloupci payment_date nějaké datum,
# ty, které nejsou zaplacené tam nemají nic - můžu použít dropna

invoices_2_paid = invoices_2.dropna().reset_index(drop=True)
invoices_2_paid["paid_in"] = invoices_2["payment_date"] - invoices_2["invoice_date"]

# chci agregovat podle názvu zákazníka, tj. groupby["customer"]
# a chci průměr - čeho??? , takže na závěr napíšu fci mean()

average_payment_data = invoices_2_paid.groupby(["customer"])["paid_in"].mean()

#převedu si formát z toho zvláštního, který vzniká z groupby na normální datetime formát
average_payment_data = pandas.DataFrame(average_payment_data)

# vytvořím si druhou tabulku, kde chci zachovat ty řádky, kde je prázdný payment_day
invoices_2_not_paid = invoices_2[invoices_2["payment_date"].isna()]

#chci propojit novou tabulku s tabulkou s těmi vypočítanými pruměry, podle jména zákazníka

invoices_2_not_paid = pandas.merge(invoices_2_not_paid, average_payment_data, on=["customer"])
# tento typ merge (pokud není specifikováno, je to inner) mi spojí jen ty zákazníky,
# kteří jsou v obou tabulkách, takže by se mi nezobrazili noví zákazníci, kteží ještě nezaplatili

#invoices_2_not_paid["expected_payment_date"] =  invoices_2_not_paid["invoice_date"] + invoices_2_not_paid["paid_invo...?? nevím co"]
invoices_2_not_paid["expected_payment_date"] =  invoices_2_not_paid["expected_payment_date"].dt.date
print(invoices_2_not_paid.head())
