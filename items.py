class Itemkategorie:
    """Darstellung der Kategorie"""
    def __init__(self, name, beschreibung):
        self.name = name
        self.beschreibung = beschreibung

    # Ich weiß nicht ob das der richtige Weg ist, aber ich möchte jeweils nur ein Objekt
    # mit einer Artikelbeschreibung -> dieses muss dann mit dem jeweiligen Item verknüpft
    # werden -> bsp:
    # Itemkategorie: Tomaten oder eine ID: 1
    # Name: Tomaten
    # Beschreibung: Tomaten sind rot


class Items:
    """stellt die items im Kühlschrank dar"""

    def __init__(self):
        pass
        # Itemkategorie("Tomate", "Tomaten sind rot",)


#Import the required libraries
from tkinter import *
from tkinter import ttk

#Create an instance of Tkinter Frame
win = Tk()

#Set the geometry
win.geometry("700x250")

# Define a function to return the Input data
def get_data():
   label.config(text= entry.get(), font= ('Helvetica 13'))

#Create an Entry Widget
entry = Entry(win, width= 42)
entry.place(relx= .5, rely= .5, anchor= CENTER)

#Inititalize a Label widget
label= Label(win, text="", font=('Helvetica 13'))
label.pack()

#Create a Button to get the input data
ttk.Button(win, text= "Click to Show", command= get_data).place(relx= .7, rely= .5, anchor= CENTER)

win.mainloop()