from tkinter import *
from tkinter import ttk
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
        item_name = ttk.Label(self.main_window, text="Artikelname:")
        item_name.grid(column=0, row=1, pady=10)

        item_cat = ttk.Label(self.main_window, text="Artikelcat:")
        item_cat.grid(column=0, row=2, pady=10)

        item_kaufdatum = ttk.Label(self.main_window, text="Kaufdatum YYYY/MM/DD:")
        item_kaufdatum.grid(column=0, row=3, pady=10)

        item_menge = ttk.Label(self.main_window, text="Menge:")
        item_menge.grid(column=2, row=1, pady=10)

        item_size = ttk.Label(self.main_window, text="Groessenangabe:")
        item_size.grid(column=2, row=2, pady=10)

        output = ttk.Label(self.main_window, text="OUTPUT")
        output.grid(column=0, row=5, pady=10)

        mhd_gekuehlt = ttk.Label(self.main_window, text="Haltbarkeitsdatum gekuehlt:")
        mhd_gekuehlt.grid(column=0, row=6, pady=10)

        mhd_ungekuehlt = ttk.Label(self.main_window, text="Haltbarkeitsdatum ungekuehlt:")
        mhd_ungekuehlt.grid(column=0, row=7, pady=10)

        output_mhd_gekuehlt = ttk.Label(self.main_window, text="Insert Data here")
        output_mhd_gekuehlt.grid(column=3, row=6, pady=10)

        output_mhd_ungekuehlt = ttk.Label(self.main_window, text="Insert Data here")
        output_mhd_ungekuehlt.grid(column=3, row=7, pady=10)

        # Entries
        item_name_entry = ttk.Entry(self.main_window)
        item_name_entry.grid(column=1, row=1, pady=10)

        item_cat_entry = ttk.Entry(self.main_window)
        item_cat_entry.grid(column=1, row=2, pady=10)

        item_kaufdatum_entry = ttk.Entry(self.main_window)
        item_kaufdatum_entry.grid(column=3, row=3, pady=10)

        item_menge_entry = ttk.Entry(self.main_window)
        item_menge_entry.grid(column=3, row=1, pady=10)

        items_size_entry = ttk.Entry(self.main_window)
        items_size_entry.grid(column=3, row=2, pady=10)

        # Buttons

        btn_add = Button(self.main_window, text="Hinzufügen")  # command=
        btn_add.grid(column=0, row=4, pady=10)

        btn_del = Button(self.main_window, text="Löschen")
        btn_del.grid(column=1, row=4, pady=10)

        self.root.mainloop()  # Ohne das mainloop startet die Erstellung des Fensters nicht
