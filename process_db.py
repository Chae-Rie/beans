import sqlalchemy
from sqlalchemy import Integer
import pymysql
import pandas as pd
import numpy as np


engine = sqlalchemy.create_engine("mysql+pymysql://root:@localhost/beans_data?charset=utf8mb4")
connection = engine.connect()

df = pd.DataFrame(np.random.randint(0, 100, (100, 3)))
df.rename({0:"A", 1:"B", 2:"C"}, axis=1, inplace=True)
print(df)

table_name = "aktueller_bestand"
df.to_sql(
    table_name,
    engine,
    if_exists='replace',  # Das muss berücksichtigt werden
    index=False,
    chunksize=500,
    dtype={
        "A": Integer,
        "B": Integer,
        "C": Integer,
    }
)
