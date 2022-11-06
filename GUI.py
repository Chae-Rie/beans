from tkinter import *
from tkinter import ttk

import process_db
from process_db import *
# ttk ist eine Art "neues" Modul um Widgets zu erstellen


class GUI():
    def __init__(self):
        # Hier können anhand der Übergabeparameter auch Werte nachgetragen werden
        # die ggf. vom Fenster bestimmt sind; Da Du nur 1x Fenster brauchst Latte
        self.root = Tk()
        self.root.title("Organize your beans!")
        self.root.geometry("700x500")

        self.main_window = ttk.Frame(self.root, padding="20")
        self.main_window.grid(column=0, row=0, sticky=(N, W, E, S))

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        """
        Abgebildet als grid lassen sich die Objekte besser strukturieren, pack() ist ungenau und place()
        ist noch nutzbar -> nur pack() ist allein nutzbar
        """

        #  Erstellen der Widgets, der übersichtlichkeitshalber

        # Labels
        self.item_name = ttk.Label(self.main_window, text="Artikelname:").grid(column=0, row=1, pady=10)

        self.item_cat = ttk.Label(self.main_window, text="Artikelcat:").grid(column=0, row=2, pady=10)

        self.item_kaufdatum = ttk.Label(self.main_window, text="Kaufdatum YYYY/MM/DD:").grid(column=0, row=3, pady=10)

        self.item_menge = ttk.Label(self.main_window, text="Menge:").grid(column=2, row=1, pady=10)

        self.item_size = ttk.Label(self.main_window, text="Groessenangabe:").grid(column=2, row=2, pady=10)

        self.output = ttk.Label(self.main_window, text="OUTPUT").grid(column=0, row=5, pady=10)

        self.mhd_gekuehlt = ttk.Label(self.main_window, text="Haltbarkeitsdatum gekuehlt:").grid(column=0,
                                                                                                 row=6,
                                                                                                 pady=10)

        self.mhd_ungekuehlt = ttk.Label(self.main_window, text="Haltbarkeitsdatum ungekuehlt:").grid(column=0,
                                                                                                     row=7,
                                                                                                     pady=10)

        self.output_mhd_gekuehlt = ttk.Label(self.main_window, text="Insert Data here").grid(column=3, row=6, pady=10)

        self.output_mhd_ungekuehlt = ttk.Label(self.main_window, text="Insert Data here").grid(column=3, row=7, pady=10)

        # Entries
        self.item_name_entry = ttk.Entry(self.main_window).grid(column=1, row=1, pady=10)

        self.item_cat_entry = ttk.Entry(self.main_window).grid(column=1, row=2, pady=10)

        self.item_kaufdatum_entry = ttk.Entry(self.main_window).grid(column=3, row=3, pady=10)

        self.item_menge_entry = ttk.Entry(self.main_window).grid(column=3, row=1, pady=10)

        self.items_size_entry = ttk.Entry(self.main_window).grid(column=3, row=2, pady=10)

        def fetch_data():
            pass
        # Holt alle Daten und schickt diese Weiter an die Datenklasse damit diese dort verarbeitet werden können


        # Buttons

        self.btn_add = Button(self.main_window, text="Hinzufügen", command=fetch_data).grid(column=0, row=4, pady=10)

        self.root.mainloop()  # Ohne das mainloop startet die Erstellung des Fensters nicht

window = GUI()


# Für Testzwecke lassen wir mainloop und die Objekterstellung in dieser Datei
