class Tile:
    def __init__(self, nearbyBombs = 0):
        self.nearbyBombs = nearbyBombs

    def __str__(self) -> str:
        return str(self.nearbyBombs)

    def get_nearbyBombs(self):
        return self.nearbyBombs

class Board:
    def __init__(self, x = 10, y = 10, bombs = 5):
        self.tiles = self.buildBoard(x, y, bombs)
        boardMatrix = self.createTileObjects(self.tiles)
        for row in boardMatrix:
            for tile in row:
                print(tile, end=" ")
            print()

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
    def __init__(self):
        self.rootWindow = self.tk.Tk()
        self.frame = self.tk.Frame(self.rootWindow)
        self.frame.grid(pady=20, padx=10)
        self.nextRow = 0

    def input(self, labelText, standardInput=""):
        self.entry = []
        self.label = []
        self.entry.append(self.tk.Entry(self.frame))
        self.label.append(self.tk.Label(self.frame, text=labelText))
        self.entry[-1].insert(0, standardInput)
        self.label[-1].grid(row=self.nextRow, column=0, sticky="e")
        self.entry[-1].grid(row=self.nextRow, column=1)
        self.nextRow += 1
    
    def button(self)
    
    def update(self):
        self.rootWindow.mainloop()
