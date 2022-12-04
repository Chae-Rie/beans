import sqlalchemy
from sqlalchemy import Integer

import pandas as pd
import numpy as np

# Herstellen der Verbindung → Da es sich um eine grundsätzliche Funktionalität handelt, muss das nicht in einer
# Memberfunktion gekapselt werden → Aber ich sollte das Nutzen von Env-Variablen in Betracht ziehen.
# Somit kann ich den Benutzernamen, den Dialekt und db-namen verschleiern
# Die ID's untereinander könnte ich ja durch die Klasse verwaltet übergeben

# TODO: Das Konzept von View, Controller und Doc ist hier doch sicher auch anwendbar oder?
# TODO: Was mache ich mit den ID's?
# TODO: Die DB ist einmal erstellt: Check; aber wie steht es um die Tabellen?
# TODO: Anpassen der []


engine = sqlalchemy.create_engine("mysql+pymysql://root:@localhost/beans_data?charset=utf8mb4")
connection = engine.connect()

df = pd.DataFrame(np.random.randint(0, 100, (2, 3)))  # Zahl von 0-100, 2 row 3 columns
df.rename({0: "A", 1: "B", 2: "C"}, axis=1, inplace=True)
print(df)


def get_current_stock(table_name):
    df.to_sql(
        table_name,
        engine,
        if_exists='append',  # append fügt die alle hinten dran, replace -> wie der Name es sagt und fail -> error
        index=False,
        chunksize=500,
        dtype={
            "A": Integer,
            "B": Integer,
            "C": Integer,
        }
    )

def create_table_kuehlschrank(table_name):
    """
    Erstellen der Tabelle zum Kühlschrank -> Ich weiß noch nicht wie ich die id verwalten möchte
    :param name: Name der Tabelle.
    :return:
    """
    data = {"id": [1],
            "standort": ["küche1"]}
    df = pd.DataFrame(data)
    print(df)

def create_table_rezept(table_name):
    data = {"id": [1],
            "beschreibung": ["Hier könnte der Text einer zufälligen Zutat stehen."],
            "zutaten": ["Hier möchte ich ein Dictionary einfuegen, was das Rezept enthält TODO"]}
    df = pd.DataFrame(data)
    print(df)

def create_table_item_kat(table_name):
    data = {"id": [1],
            "artikelbeschreibung": ["Hier könnte eine Beschreibung zu einer Art von Artikel stehen"]}
    df = pd.DataFrame(data)
    print(df)

def create_table_receipt(table_name):
    data = {"id": [1],
            "items_gesamt": ["Zahl der gekauften Items"],
            "Summe in EUR": [2.50]}
    df = pd.DataFrame(data)
    print(df)
    pass

def create_table_items(table_name):
    data = {"id": [1],
            "menge": [1.50],  # decimal, weil es auch (kilo)-gramm sein können
            "groessenangabe": ["STK oder KG"],
            "gekauft_am": ["2022-11-10"],
            "haltbar_bis_ungekuehlt": ["2022-11-20"],
            "haltbar_bis_gekuehlt": ["2022-11-22"]
            }
    df = pd.DataFrame(data)
    print(df)