import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import create_engine, inspect

HOST = "czechitaspsql.postgres.database.azure.com"
PORT = 5432
USER = "katroskaa"
USERNAME = f"{USER}@czechitaspsql"
DATABASE = "postgres"
PASSWORD = "4KO32ykboR7zJqaM"

engine = create_engine(f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}", echo=False)

inspector = inspect(engine)
#print(inspector.get_table_names())

df = pd.read_sql("dreviny", con=engine)
desired_width = 1000
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',100)

smrk = pd.read_sql("SELECT * from dreviny WHERE dd_txt = 'Smrk, jedle, douglaska'", con=engine)
nahodila_tezba = pd.read_sql("SELECT * from dreviny WHERE druhtez_txt = 'Nahodilá těžba dřeva'", con=engine)

print(smrk.head())
smrk_pivot = pd.pivot_table(smrk, index="rok", columns="dd_txt", values="hodnota",
                                      aggfunc=np.sum)
smrk_pivot.plot()
plt.show()

nahodila_tezba_pivot = pd.pivot_table(nahodila_tezba, index="rok", columns="prictez_txt", values="hodnota",
                                      aggfunc=np.sum)
print(nahodila_tezba_pivot)
nahodila_tezba_pivot.plot()
plt.show()