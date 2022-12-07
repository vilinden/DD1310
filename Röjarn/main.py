from classes import *

class Program:
    def main(self):
        self.gui = GUI(self)
        while True:    
            self.boardWidth, self.boardHeight, self.amountOfBombs = 0,0,0
            try:
                self.getBoardSettings()
                break
            except:
                self.gui.newWindow()

        self.board = Board(self.boardWidth, self.boardHeight, self.amountOfBombs)
        self.tileBoxes = []
        for row in self.board.get_matrix():
            y = self.board.get_matrix().index(row)
            for tile in row:
                x = row.index(tile)
                self.tileBoxes.append(self.gui.drawTile(tile, x, y))
        self.gui.update()

    def getBoardSettingsData(self):
        data = self.gui.getEntryData()
        self.boardWidth = int(data[0])
        self.boardHeight = int(data[1])
        self.amountOfBombs = int(data[2])
        self.gui.newWindow()
        

    def getBoardSettings(self):
        self.gui.input("Width:", 10)
        self.gui.input("Height:", 10)
        self.gui.input("Bombs:", 5)
        self.gui.button("Start", lambda : self.getBoardSettingsData())
        self.gui.update()

    def recursiveOpen(self, tileBox, tile):
        # Checking win recursivly from tile
        currentTileCoordinates = []
        for row in self.board.get_matrix():
            if tile in row:
                currentTileCoordinates = [row.index(tile), self.board.get_matrix().index(row)]
                break

        checkCoords = [
                    {"x": currentTileCoordinates[0]-1,  "y": currentTileCoordinates[1]-1},  #top right
                    {"x": currentTileCoordinates[0]-1,  "y": currentTileCoordinates[1]},    #top middle
                    {"x": currentTileCoordinates[0]-1,  "y": currentTileCoordinates[1]+1},  #top left
                    {"x": currentTileCoordinates[0],    "y": currentTileCoordinates[1]-1},  #left
                    {"x": currentTileCoordinates[0],    "y": currentTileCoordinates[1]+1},  #right
                    {"x": currentTileCoordinates[0]+1,  "y": currentTileCoordinates[1]-1},  #bottom right
                    {"x": currentTileCoordinates[0]+1,  "y": currentTileCoordinates[1]},    #bottom middle
                    {"x": currentTileCoordinates[0]+1,  "y": currentTileCoordinates[1]+1},  #bottom left
        ]

        for coords in checkCoords:
            if coords["x"] >= 0 and coords["y"] >= 0:
                if coords["x"] < len(self.board.get_matrix()[0]) and coords["y"] < len(self.board.get_matrix()):
                    nextTile = self.board.get_matrix()[coords["y"]][coords["x"]]
                    nextTileBox = self.tileBoxes[coords["y"]*len(self.board.get_matrix()) + coords["x"]]
                    if nextTile.get_open() == False:
                        self.gui.openTile(nextTileBox, nextTile)

    def checkWinFlag(self):
        win = True
        for row in self.board.get_matrix():
            if win:
                for tile in row:
                    if tile.get_flagged() and tile.get_nearbyMines() != 9:
                        win = False
                    elif (not tile.get_flagged()) and tile.get_nearbyMines() == 9:
                        win = False

        if win: 
            self.openAllTiles()
            print("WIN") #win

    def checkWinOpen(self):
        win = True
        for row in self.board.get_matrix():
            if win:
                for tile in row:
                    if (not tile.get_open()) and tile.get_nearbyMines() != 9:
                        win = False

        if win: 
            self.openAllTiles()
            print("WIN") #win

    def openAllTiles(self):
        for i in range(len(self.tileBoxes)):
            box = self.tileBoxes[i]
            tile = self.board.get_matrix()[int(i/len(self.board.get_matrix()))][i%len(self.board.get_matrix()[0])]
            if not tile.get_open:
                self.gui.openTile(box, tile, explodeBomb=False)

        self.gui.update()


if __name__ == "__main__":
    program = Program()
    program.main()