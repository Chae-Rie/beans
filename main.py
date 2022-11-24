# TestCommit durch jetbrains IDE
from GUI import GUI
from items import Itemkategorie, Items
from process_db import Db

db = Db(3306, "beans_data")
engine = db.connect_db()
df = db.create_data()
db.create_table("Aktueller Stand 2022-11-24", df, engine)
