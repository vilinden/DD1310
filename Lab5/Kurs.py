# Viktor Lindén, Erik Stare
# 2022-10-03

# Klass för kurs
class Kurs:
    # Funktion som initierar kursobjekt
    def __init__(self, namn, poäng):
        self.namn = namn
        self.poäng = poäng
        self.avklarad = False
    
    # Funktion som ger sträng av kursen.
    def __str__(self):
        return self.namn + " - " + str(self.poäng) + " - Avklarad: " + str(self.avklarad)