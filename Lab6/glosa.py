# Viktor Lindén, Erik Stare
# 2022-10-04

# Klass för glosor
class Glosa:
    #Funktion som initierar glosobjekt
    def __init__(self, svenska, engelska, rätt=0, fel=0):
        self.__svenska = svenska
        self.__engelska = engelska
        self.__rätt = rätt
        self.__fel = fel
        self.__senaste = "Fel"

    def __str__(self):
        return "{:<10}{:<10}{:<8}{}".format(self.__svenska, self.__engelska, self.__senaste, str(self.__rätt) + "/" + str(int(self.__rätt) + int(self.__fel)))

    def addCorrect(self):
        self.__rätt += 1
        self.__senaste = "Rätt"
    
    def addWrong(self):
        self.__fel += 1
        self.__senaste = "Fel"

    def getRätt(self):
        return self.__rätt
    def getFel(self):
        return self.__fel

    def getSvenska(self):
        return self.__svenska
    def getEngelska(self):
        return self.__engelska