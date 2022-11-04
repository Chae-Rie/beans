from tkinter import *
from tkinter import ttk
# ttk ist eine Art "neues" Modul um Widgets zu erstellen


class GUI():
    def __init__(self):
        # Hier können anhand der Übergabeparameter auch Werte nachgetragen werden
        # die ggf. vom Fenster bestimmt sind; Da Du nur 1x Fenster brauchst Latte
        self.root = Tk()
        self.root.title("Organize your beans!")
        self.root.geometry("500x500")

        self.main_window = ttk.Frame(self.root, padding="3 3 12 12")
        self.main_window.grid(column=0, row=0, sticky=(N, W, E, S))

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        """
        Abgebildet als grid lassen sich die Objekte besser strukturieren, pack() ist ungenau und place()
        ist noch nutzbar -> nur pack() ist allein nutzbar
        """

        #  Erstellen der Widgets, der übersichtlichkeitshalber

        # Buttons


        # Entries
        item_entry = ttk.Entry(self.main_window)
        item_entry.grid(column=1, row=0)


        self.root.mainloop()  # Ohne das mainloop startet die Erstellung des Fensters nicht
