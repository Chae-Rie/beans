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
