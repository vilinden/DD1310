import datetime
from classes import *
import os

def main():
    program = Program()
    program.main()

class Program:
    def main(self):
        self.top10Path = os.path.realpath(os.path.dirname(__file__)) + "/top10.txt"
        self.gui = GUI(self)
        self.top10list = self.readFile()
        self.score = 0
        self.startTime = datetime.datetime.now()
        self.winTime = 0
        while True:    
            self.boardWidth, self.boardHeight, self.amountOfBombs = 0,0,0
            try:
                self.getBoardSettings()
                break
            except:
                self.gui.newWindow()

        self.board = Board(self.boardWidth, self.boardHeight, self.amountOfBombs)
        self.tileBoxes = []
        for row in self.board.getMatrix():
            y = self.board.getMatrix().index(row)
            for tile in row:
                x = row.index(tile)
                self.tileBoxes.append(self.gui.drawTile(tile, x, y))
        self.gui.drawQuitReset()
        self.gui.update()

    def getBoardSettingsData(self):
        data = self.gui.getEntryData()
        try:
            self.boardWidth = int(data[0])
            self.boardHeight = int(data[1])
            self.amountOfBombs = int(data[2])
            if self.boardWidth > 40 or self.boardHeight > 20 or self.amountOfBombs > self.boardHeight*self.boardWidth:
                raise
            elif self.amountOfBombs <= 0 or self.boardHeight <= 0 or self.boardWidth <= 0:
                raise
            self.gui.newWindow()
        except:
            self.gui.drawLabel("Invalid input", checkDouble = True, sticky="e", column=1, textColor="red")
        

    def getBoardSettings(self):
        self.gui.drawInput("Width (Max 40):", 10)
        self.gui.drawInput("Height (Max 20):", 10)
        self.gui.drawInput("Bombs:", 5)
        self.gui.drawButton("Start", self.getBoardSettingsData, newLine=False)
        self.gui.drawButton("Quit", self.quit, column=1, sticky="e")
        self.gui.update()

    def recursiveOpen(self, tile):
        # Checking win recursivly from tile
        currentTileCoordinates = []
        for row in self.board.getMatrix():
            if tile in row:
                currentTileCoordinates = [row.index(tile), self.board.getMatrix().index(row)]
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
                if coords["x"] < len(self.board.getMatrix()[0]) and coords["y"] < len(self.board.getMatrix()):
                    nextTile = self.board.getMatrix()[coords["y"]][coords["x"]]
                    nextTileBox = self.tileBoxes[coords["y"]*len(self.board.getMatrix()) + coords["x"]]
                    if nextTile.getOpen() == False:
                        self.gui.openTile(nextTileBox, nextTile)

    def checkWinFlag(self):
        win = True
        for row in self.board.getMatrix():
            if win:
                for tile in row:
                    if tile.getFlagged() and tile.getNearbyMines() != 9:
                        win = False
                    elif (not tile.getFlagged()) and tile.getNearbyMines() == 9:
                        win = False

        if win: 
            self.win()

    def checkWinOpen(self):
        win = True
        for row in self.board.getMatrix():
            if win:
                for tile in row:
                    if (not tile.getOpen()) and tile.getNearbyMines() != 9:
                        win = False

        if win: 
            self.win()

    def win(self):
        self.winTime = datetime.datetime.now() - self.startTime
        self.score = (self.amountOfBombs/(self.boardWidth * self.boardHeight))*1000/self.winTime.total_seconds()
        self.openAllTiles()
        self.gui.drawWin(self.winTime, self.score)

    def openAllTiles(self):
        for i in range(len(self.tileBoxes)):
            box = self.tileBoxes[i]
            tile = self.board.getMatrix()[int(i/len(self.board.getMatrix()))][i%len(self.board.getMatrix()[0])]
            if not tile.getOpen():
                self.gui.openTile(box, tile, explodeBomb=False, checkWin = False)


    def readFile(self):
        lines = []
        try:
            f = open(self.top10Path, "r", encoding="ASCII")
            lines = f.readlines()
            for i in range(len(lines)):
                lines[i] = lines[i].removesuffix("\n")
        except:
            f = open(self.top10Path, "x")
        f.close()
        return lines

    def saveScore(self, button):
        try:
            if type(self.top10list[0]) != list:
                for result in self.top10list:
                    splittedResult = result.split(":")
                    splittedResult[1] = float(splittedResult[1])
                    self.top10list[self.top10list.index(result)] = splittedResult
            name = self.gui.getEntryData()[0]
            if len(name) < 1 or len(name) > 15:
                raise
            self.top10list.append([name, self.score])
            self.top10list = sorted(self.top10list, key=lambda list: list[1])[::-1]
            f = open(self.top10Path, "w", encoding="ASCII")
            for i in range(10):
                f.write(self.top10list[i][0]+":"+str(self.top10list[i][1])+"\n")
            f.close()
        except Exception as err:
            print(err)
            self.gui.drawLabel("Couldn't save to file!", columnSpan=4, checkDouble=True, textColor="red")
        button.config(state = "disabled")
        button.config(text = "Saved!")

    def showTop10(self):
        top10 = self.readFile()
        for i in range(len(top10)):
            top10[i] = top10[i].split(":")
        self.gui.drawTop10(top10)
        pass

    def loose(self):
        self.openAllTiles()
        self.gui.drawLoose()

    def restart(self):
        self.gui.destroy()
        self.main()

    def quit(self):
        self.gui.destroy()

if __name__ == "__main__":
    main()