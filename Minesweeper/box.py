class Box:
    def __init__(self):
        self.__nearby = 0
        self.__mine = False
        self.__flagged = False
        self.__open = False

    def __str__(self):
        if self.__mine:
            return "X"
        else: return "O"

    def setMine(self):
        self.__mine = True
    def getMine(self):
        return self.__mine

    def setNearby(self, nearby: int):
        self.__nearby = nearby
    def getNearby(self):
        return self.__nearby

    def setFlagged(self, flagged: bool):
        self.__flagged = flagged
    def getFlagged(self):
        return self.__flagged

    def open(self):
        self.__open = True
    def isOpen(self):
        return self.__open
