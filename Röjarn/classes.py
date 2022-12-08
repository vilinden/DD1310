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
        self.blankPath = "./img/blank.png"
        self.flagPath = "./img/flag.png"
        self.background = "white"
        self.rootWindow = self.tk.Tk(className = "Minesweeper")
        self.rootWindow.config(bg=self.background)
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
        self.frame = self.tk.Frame(self.rootWindow, background=self.background)
        self.frame.grid(padx=20, pady=20)
        self.nextRow = 0
        self.entry = []
        self.label = []
        self.btn = []

    def set_background(self, color):
        self.background = color
        self.frame.configure(background=self.background)

    def drawTile(self, tile, x, y):
        t = tile.get_nearbyMines()
        tileBox = self.tk.Label(self.frame, image = self.tileImage["blank"], text=t)
        tileBox.grid(column = x, row = y)
        tileBox.bind("<Button-1>", lambda a : self.openTile(tileBox, tile))
        tileBox.bind("<Button-2>", lambda b : self.flagTile(tileBox, tile))
        tileBox.bind("<Button-3>", lambda c : self.flagTile(tileBox, tile))
        return tileBox

    def drawInput(self, labelText, standardInput="", column = 1, sticky = ""):
        self.entry.append(self.tk.Entry(self.frame))
        self.drawLabel(labelText, sticky = "e", newLine=False)
        self.entry[-1].insert(0, standardInput)
        self.entry[-1].grid(row=self.nextRow, column=column, sticky=sticky)
        self.nextRow += 1
    
    def drawButton(self, btnText, func, column = 0, sticky = "", newLine = True):
        self.btn.append(self.tk.Button(self.frame, text=btnText, command=func))
        self.btn[-1].grid(row=self.nextRow, column = column, sticky=sticky)
        self.nextRow += 1*newLine
    
    def drawLabel(self, text, column = 0, sticky = "", newLine = True, checkDouble = False, textColor = "black"):
        if checkDouble:
            for label in self.label:
                if label.cget('text') == text:
                    return
        self.label.append(self.tk.Label(self.frame, text=text, background=self.background, foreground=textColor))
        self.label[-1].grid(row=self.nextRow, column=column, sticky=sticky)
        self.nextRow += 1*newLine
        
    def getEntryData(self):
        returnData = []
        for entry in self.entry:
            returnData.append(entry.get())
        return returnData

    def openTile(self, tileBox, tile, explodeBomb = True):
        showImg = tile.get_nearbyMines()
        tile.set_open()
        if showImg == 9 and explodeBomb:
            showImg = "explode"
            tileBox.config(image = self.tileImage[showImg])
            self.parent.loose()
            return
        tileBox.config(image = self.tileImage[showImg])
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

    def drawLoose(self):
        self.background = "red"
        self.createToplevel()
        self.drawLabel("You Lost!")
        self.drawButton("Restart", self.parent.restart, sticky="w", newLine=False)
        self.drawButton("Quit", self.parent.quit, column=1, sticky="e")
        print("A")
        self.update()

    def createToplevel(self):
        self.toplevel = self.tk.Toplevel(self.rootWindow, background=self.background)
        self.toplevel.grab_set()
        self.toplevel.config(bg=self.background)
        self.frame = self.tk.Frame(self.toplevel, background=self.background)
        self.frame.grid(padx=20, pady=20)

    def update(self):
        try:
            self.toplevel.mainloop()
        except:
            self.rootWindow.mainloop()
   