import sqlalchemy
import pandas as pd
import numpy as np

class Db:
    '''
    - Erstellen der DB
    - CRUD-Functions
    '''
    def __int__(self, db_port,db_name):
        self.db_type = 'mysql+pymsql'
        self.db_port = db_port  # in dem Fall 3306
        self.db_name = db_name  # Name der Database


    def connect_db(self):
        engine = sqlalchemy.create_engine(f'{self.db_type}://root:@localhost:{self.db_port}/{self.db_name}')
        # engine = sqlalchemy.create_engine('mysql+pymysql://root:@localhost:3306/beans_data')
        conn = engine.connect()

    def create_data(self):
        df = pd.DataFrame(np.random.randint(0, 100, (20, 2)))
        df.rename({0:"FirstCol", 1:"SecondCol"}, axis=1, inplace=True)
    def create_table(self, name):  # aktueller Bestand
        table_name = name  # z.B.: könnte die Tabelle einfach ein Datum sein YYYY-MM-DD // Oder aktueller Bestand
        df.to_sql()


