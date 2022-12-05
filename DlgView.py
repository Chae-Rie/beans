from tkinter import ttk
import tkinter as tk

import pandas as pd


class Window_Start:
    """Visuals der Desktop-Anwendung"""
    def __init__(self, master):
        # Hier können anhand der Übergabeparameter auch Werte nachgetragen werden
        # die ggf. vom Fenster bestimmt sind; Da Du nur 1x Fenster brauchst Latte

        self.master = master
        self.master.title("Organize your beans!")
        self.master.geometry("700x500")

        self.frame = ttk.Frame(self.master, padding="20")
        self.frame.grid(column=0, row=0, sticky="N, W, E, S")

        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        """
        Abgebildet als grid lassen sich die Objekte besser strukturieren, pack() ist ungenau und place()
        ist noch nutzbar -> nur pack() ist allein nutzbar
        """

        #  Erstellen der Widgets, der übersichtlichkeitshalber

        # Labels
        self.item_name_label = ttk.Label(self.frame, text="Artikelname:")
        self.item_name_label.grid(column=0, row=1, pady=10)

        self.item_cat_label = ttk.Label(self.frame, text="Artikelcat:")
        self.item_cat_label.grid(column=0, row=2, pady=10)

        self.item_purchase_date_label = ttk.Label(self.frame, text="Kaufdatum YYYY/MM/DD:")
        self.item_purchase_date_label.grid(column=0, row=3, pady=10)

        self.item_amount_label = ttk.Label(self.frame, text="Menge:")
        self.item_amount_label.grid(column=2, row=1, pady=10)

        self.item_size_label = ttk.Label(self.frame, text="Groessenangabe:")
        self.item_size_label.grid(column=2, row=2, pady=10)

        self.output_label = ttk.Label(self.frame, text="OUTPUT")
        self.output_label.grid(column=0, row=5, pady=10)

        self.mhd_gekuehlt_label = ttk.Label(self.frame, text="Haltbarkeitsdatum gekuehlt:")
        self.mhd_gekuehlt_label.grid(column=0, row=6, pady=10)

        self.mhd_ungekuehlt_label = ttk.Label(self.frame, text="Haltbarkeitsdatum ungekuehlt:")
        self.mhd_gekuehlt_label.grid(column=0, row=7, pady=10)

        self.output_mhd_gekuehlt_label = ttk.Label(self.frame, text="Insert Data here")
        self.output_mhd_gekuehlt_label.grid(column=3, row=6, pady=10)

        self.output_mhd_ungekuehlt_label = ttk.Label(self.frame, text="Insert Data here")
        self.output_mhd_ungekuehlt_label.grid(column=3, row=7, pady=10)

        # Entries
        self.item_name = tk.StringVar(self.master)
        self.item_name_entry = ttk.Entry(self.frame, textvariable=self.item_name)
        self.item_name_entry.grid(column=1, row=1, pady=10)

        self.item_cat = tk.StringVar(self.master)
        self.item_cat_entry = ttk.Entry(self.frame, textvariable=self.item_cat)
        self.item_cat_entry.grid(column=1, row=2, pady=10)

        self.item_purchase_date = tk.StringVar(self.master)
        self.item_purchase_data_entry = ttk.Entry(self.frame, textvariable=self.item_purchase_date)
        self.item_purchase_data_entry.grid(column=3, row=3, pady=10)

        self.item_amount = tk.StringVar(self.master)
        self.item_amount_entry = ttk.Entry(self.frame, textvariable=self.item_amount)
        self.item_amount_entry.grid(column=3, row=1, pady=10)

        self.item_size = tk.StringVar(self.master)
        self.items_size_entry = ttk.Entry(self.frame, textvariable=self.item_size)
        self.items_size_entry.grid(column=3, row=2, pady=10)
        # Buttons

        self.btn_add = tk.Button(self.frame, text="Hinzufügen", command=self.fetch_data)
        self.btn_add.grid(column=0, row=4, pady=10)

    def fetch_data(self):
        # add all data into a dictionary I think
        data = {
            "Menge:": [self.item_amount.get()],
            "ItemCat:": [self.item_cat.get()],
            "ItemName:": [self.item_name.get()],
            "Gekauft am:": [self.item_purchase_date.get()],
            "Item Größe:": [self.item_size.get()]
        }
        df_data = pd.DataFrame(data)
        print(df_data)

# test = "Hello: {0},{1}".format("You", "and me.")
# print(test) So kann ich die Argumente effektiv übergeben


class result_screen:
    """Anstatt die Ergebnisse in demselben Fenster auszugeben, möchte ich hier ein neues tkinter-Fenster öffnen
    in diesem soll dann die Tabelle, die direkt mit der DB verbunden ist, dargestellt werden."""
    def __init__(self, master):
        self.master = master


# def main():
#     """In dieser Methode können wir alles an Logik hinzufügen und anschließend wird es in Main getriggered."""
#     root = tk.Tk()
#     app = Window_Start(root)
#     root.mainloop()
#
#
# if __name__ == '__main__':
#     main()
