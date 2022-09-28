# Klass för glosor
class Glosa:
    #Funktion som initierar glosobjekt
    def __init__(self, svenska, engelska):
        self.svenska = svenska
        self.engelska = engelska
    def __str__(self):
        return self.svenska+" "+self.engelska