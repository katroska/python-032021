import pandas as pd
import numpy as np
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

df = pd.read_sql("crime", con=engine)
#print(df.head())
desired_width = 1000
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',100)


vehicle_theft = pd.read_sql("SELECT * from crime WHERE \"PRIMARY_DESCRIPTION\" = 'MOTOR VEHICLE THEFT'", con=engine)
vehicle_theft = vehicle_theft[vehicle_theft["SECONDARY_DESCRIPTION"].str.contains("automobile", case=False)]
#print(vehicle_theft)
vehicle_theft["Month"] = pd.to_datetime(vehicle_theft["DATE_OF_OCCURRENCE"]).dt.strftime("%Y/%m")
vehicle_theft_grouped = vehicle_theft.groupby("Month").size()
print(vehicle_theft_grouped.idxmax(), vehicle_theft_grouped.max())
# aby byl vidět i měsíc, použiji metodu idxmax, kt. zobrazí index u max hodnoty
