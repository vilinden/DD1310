class Tile:
    def __init__(self, nearbyMines = 0):
        self.nearbyMines = nearbyMines
        self.flagged = False
        self.open = False

    def get_nearbyMines(self):
        return self.nearbyMines

    def set_open(self):
        self.open = True

    def get_open(self):
        return self.open
    
    def set_flagged(self):
        self.flagged = True

    def get_flagged(self):
        return self.flagged
    
    def set_unflagged(self):
        self.flagged = False

class Board:
    def __init__(self, x = 10, y = 10, bombs = 5):
        self.tiles = self.buildBoard(x, y, bombs)
        self.boardMatrix = self.createTileObjects(self.tiles)

    def __str__(self):
        returnStr = ""
        for row in self.boardMatrix:
            for col in row:
                returnStr += str(col) + " "
            returnStr += "\n"

        return returnStr

    def get_matrix(self):
        return self.boardMatrix

    def buildBoard(self, x, y, bombs):
        tiles = []
        for row in range(y):
            tiles.append([])
            for col in range(x):
                tiles[row].append(0)

        mineCoordinates = self.selectMineTiles(x, y, bombs)

        for coords in mineCoordinates:
            tiles[coords[1]][coords[0]] = 9
    
        tiles = self.checkNearbyMines(tiles)
        return tiles

    def selectMineTiles(self, x, y, bombs):
        import random
        totalTiles = list(range(x*y))
        mines = []
        for i in range(bombs):
            tileID = random.choice(totalTiles)
            mines.append([tileID%x, int(tileID/x)])
            totalTiles.remove(tileID)
        return mines

    def checkNearbyMines(self, tiles):
        for row in range(len(tiles)):
            for tile in range(len(tiles[0])):
                nearbyMines = 0

                # Coordinates of tiles surrounding current tile
                checkCoords = [
                    {"x": tile-1,  "y": row-1},  #top right
                    {"x": tile-1,  "y": row},    #top middle
                    {"x": tile-1,  "y": row+1},  #top left
                    {"x": tile,    "y": row-1},  #left
                    {"x": tile,    "y": row+1},  #right
                    {"x": tile+1,  "y": row-1},  #bottom right
                    {"x": tile+1,  "y": row},    #bottom middle
                    {"x": tile+1,  "y": row+1},  #bottom left
                ]
                for coord in checkCoords:
                    try:
                        if coord["x"] < 0 or coord["y"] < 0:
                            raise
                        else:
                            if tiles[coord["y"]][coord["x"]] == 9:
                                nearbyMines += 1
                    except:
                        pass
                
                if tiles[row][tile] != 9:
                    tiles[row][tile] = nearbyMines

        return tiles
    
    def createTileObjects(self, tiles):
        boardMatrix = []
        for row in tiles:
            boardMatrix.append([])
            for tile in row:
                boardMatrix[-1].append(Tile(tile))

        return boardMatrix

class GUI:
    import tkinter as tk
    def __init__(self, parent):
        self.parent = parent
        self.rootWindow = self.tk.Tk()
        self.blankPath = "./img/blank.png"
        self.flagPath = "./img/flag.png"
        self.tileImage = {
            "blank" : self.tk.PhotoImage(file = self.blankPath),
            "flag" : self.tk.PhotoImage(file = self.flagPath),
            "explode" : self.tk.PhotoImage(file = "./img/explode.png"),
            0 : self.tk.PhotoImage(file = "./img/0.png"),
            1 : self.tk.PhotoImage(file = "./img/1.png"),
            2 : self.tk.PhotoImage(file = "./img/2.png"),
            3 : self.tk.PhotoImage(file = "./img/3.png"),
            4 : self.tk.PhotoImage(file = "./img/4.png"),
            5 : self.tk.PhotoImage(file = "./img/5.png"),
            6 : self.tk.PhotoImage(file = "./img/6.png"),
            7 : self.tk.PhotoImage(file = "./img/7.png"),
            8 : self.tk.PhotoImage(file = "./img/8.png"),
            9 : self.tk.PhotoImage(file = "./img/bomb.png")
        }
        self.frame = self.tk.Frame(self.rootWindow)
        self.frame.grid(pady=20, padx=10)
        self.nextRow = 0
        self.entry = []
        self.label = []
        self.btn = []

    def drawTile(self, tile, x, y):
        t = tile.get_nearbyMines()
        tileBox = self.tk.Label(self.frame, image = self.tileImage["blank"], text=t)
        tileBox.grid(column = x, row = y)
        tileBox.bind("<Button-1>", lambda a : self.openTile(tileBox, tile))
        tileBox.bind("<Button-2>", lambda b : self.flagTile(tileBox, tile))
        tileBox.bind("<Button-3>", lambda c : self.flagTile(tileBox, tile))
        return tileBox

    def input(self, labelText, standardInput=""):
        self.entry.append(self.tk.Entry(self.frame))
        self.label.append(self.tk.Label(self.frame, text=labelText))
        self.entry[-1].insert(0, standardInput)
        self.label[-1].grid(row=self.nextRow, column=0, sticky="e")
        self.entry[-1].grid(row=self.nextRow, column=1)
        self.nextRow += 1
    
    def button(self, btnText, func):
        self.btn.append(self.tk.Button(self.frame, text=btnText, command=func))
        self.btn[-1].grid(row=self.nextRow, column = 0)
        self.nextRow += 1
        
    def getEntryData(self):
        returnData = []
        for entry in self.entry:
            returnData.append(entry.get())
        return returnData

    def openTile(self, tileBox, tile, explodeBomb = True):
        showImg = tile.get_nearbyMines()
        if showImg == 9 and explodeBomb:
            showImg = "explode"
        tileBox.config(image = self.tileImage[showImg])
        tile.set_open()
        self.parent.checkWinOpen()
        if showImg == 0:
            self.parent.recursiveOpen(tileBox, tile)

    def flagTile(self, tileBox, tile):
        try:
            if self.rootWindow.call(tileBox.cget('image'), 'cget', '-file') == self.blankPath:
                tileBox.config(image = self.tileImage["flag"])
                tile.set_flagged()
            elif self.rootWindow.call(tileBox.cget('image'), 'cget', '-file') == self.flagPath:
                tileBox.config(image = self.tileImage["blank"])
                tile.set_unflagged()
            
            self.parent.checkWinFlag()
        except:
            pass

    def newWindow(self):
        self.rootWindow.destroy()
        self.rootWindow.quit()
        self.__init__(self.parent)

    def update(self):
        self.rootWindow.mainloop()
