import tkinter
from tkinter import *
from tkinter import ttk


class GUI:
    '''Visuals der Desktop-Anwendung'''

    def __init__(self):
        # Hier können anhand der Übergabeparameter auch Werte nachgetragen werden
        # die ggf. vom Fenster bestimmt sind; Da Du nur 1x Fenster brauchst Latte
        self.root = Tk()
        self.root.title("Organize your beans!")
        self.root.geometry("700x500")

        self.main_window = ttk.Frame(self.root, padding="20")
        self.main_window.grid(column=0, row=0, sticky="N, W, E, S")

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        """
        Abgebildet als grid lassen sich die Objekte besser strukturieren, pack() ist ungenau und place()
        ist noch nutzbar -> nur pack() ist allein nutzbar
        """

        #  Erstellen der Widgets, der übersichtlichkeitshalber

        # Labels
        self.item_name_label = ttk.Label(self.main_window, text="Artikelname:")
        self.item_name_label.grid(column=0, row=1, pady=10)

        self.item_cat_label = ttk.Label(self.main_window, text="Artikelcat:")
        self.item_cat_label.grid(column=0, row=2, pady=10)

        self.item_purchase_date_label = ttk.Label(self.main_window, text="Kaufdatum YYYY/MM/DD:")
        self.item_purchase_date_label.grid(column=0, row=3, pady=10)

        self.item_amount_label = ttk.Label(self.main_window, text="Menge:")
        self.item_amount_label.grid(column=2, row=1, pady=10)

        self.item_size_label = ttk.Label(self.main_window, text="Groessenangabe:")
        self.item_size_label.grid(column=2, row=2, pady=10)

        self.output_label = ttk.Label(self.main_window, text="OUTPUT")
        self.output_label.grid(column=0, row=5, pady=10)

        self.mhd_gekuehlt_label = ttk.Label(self.main_window, text="Haltbarkeitsdatum gekuehlt:")
        self.mhd_gekuehlt_label.grid(column=0, row=6, pady=10)

        self.mhd_ungekuehlt_label = ttk.Label(self.main_window, text="Haltbarkeitsdatum ungekuehlt:")
        self.mhd_gekuehlt_label.grid(column=0, row=7, pady=10)

        self.output_mhd_gekuehlt_label = ttk.Label(self.main_window, text="Insert Data here")
        self.output_mhd_gekuehlt_label.grid(column=3, row=6, pady=10)

        self.output_mhd_ungekuehlt_label = ttk.Label(self.main_window, text="Insert Data here")
        self.output_mhd_ungekuehlt_label.grid(column=3, row=7, pady=10)

        # Entries
        self.item_name = tkinter.StringVar(self.root)
        self.item_name_entry = ttk.Entry(self.main_window, textvariable=self.item_name)
        self.item_name_entry.grid(column=1, row=1, pady=10)

        self.item_cat = tkinter.StringVar(self.root)
        self.item_cat_entry = ttk.Entry(self.main_window, textvariable=self.item_cat)
        self.item_cat_entry.grid(column=1, row=2, pady=10)

        self.item_purchase_date = tkinter.StringVar(self.root)
        self.item_purchase_data_entry = ttk.Entry(self.main_window, textvariable=self.item_purchase_date)
        self.item_purchase_data_entry.grid(column=3, row=3, pady=10)

        self.item_amount = tkinter.StringVar(self.root)
        self.item_amount_entry = ttk.Entry(self.main_window, textvariable=self.item_amount)
        self.item_amount_entry.grid(column=3, row=1, pady=10)

        self.item_size = tkinter.StringVar(self.root)
        self.items_size_entry = ttk.Entry(self.main_window, textvariable=self.item_size)
        self.items_size_entry.grid(column=3, row=2, pady=10)
        # Buttons

        self.btn_add = Button(self.main_window, text="Hinzufügen", command=self.fetch_data)
        self.btn_add.grid(column=0, row=4, pady=10)

        self.root.mainloop()  # Ohne das mainloop startet die Erstellung des Fensters nicht

    def fetch_data(self):
        # add all data into a dictionary I think
        print(self.item_amount.get(),
              self.item_cat.get(),
              self.item_name.get(),
              self.item_purchase_date.get(),
              self.item_size.get())

# test = "Hello: {0},{1}".format("You", "and me.")
# print(test) So kann ich die Argumente effektiv übergeben
window = GUI()

# Für Testzwecke lassen wir mainloop und die Objekterstellung in dieser Datei
