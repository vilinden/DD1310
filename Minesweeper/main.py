from tile import Tile
import random
from tkinter import *
from tkinter import ttk
from datetime import datetime

x,y,m = 0,0,0 

# Huvudfunktion för att köra programmet
def main():
    while True:
        print("Starting game loop...")
        window = Tk()
        window.resizable(False, False)
        window.title("Minesweeper")
        size, mineCount, window = defInitials(window)
        print("Setting up game with your settings.", end="")
        global x
        if x == 0:
            quit()
        board = []
        for y in range(size[1]):
            row = []
            for x in range(size[0]):
                row.append(Tile(x,y,window))
            board.append(row)
        
        mines = random.sample(range(len(board[0])*len(board)), mineCount)
        for i in mines:
            y = int(i/len(board[0]))
            x = i%len(board[0])
            board[y][x].setMine()

        for row in board:
            for tile in row:
                tile.setTotalMines(mineCount)
                neighbors = []
                coords = [
                    {"x": tile.x-1,  "y": tile.y-1},  #top right
                    {"x": tile.x-1,  "y": tile.y},    #top middle
                    {"x": tile.x-1,  "y": tile.y+1},  #top left
                    {"x": tile.x,    "y": tile.y-1},  #left
                    {"x": tile.x,    "y": tile.y+1},  #right
                    {"x": tile.x+1,  "y": tile.y-1},  #bottom right
                    {"x": tile.x+1,  "y": tile.y},    #bottom middle
                    {"x": tile.x+1,  "y": tile.y+1},  #bottom left
                ]
                for coord in coords:
                    try:
                        if coord["x"] < 0 or coord["y"] < 0:
                            raise
                        neighbors.append(board[coord["y"]][coord["x"]])
                    except:
                        pass
                
                neighborMines = 0
                for n in neighbors:
                    if n.getMine():
                        neighborMines += 1

                tile.setNearby(neighborMines)
                tile.setNearbyTiles(neighbors)

        print(".", end="")
        draw(board,window)



# Definierar initialvärden för brädesstorlek och antalet minor
def defInitials(window):
    print("Initiating...")
    frame = ttk.Frame(window, padding=10)
    frame.grid(pady=10)
    Label(frame, text="Rows (MAX 20):").grid(row=1, pady=5, sticky="e")
    Label(frame, text="Columns (MAX 40):").grid(row=2, pady=5, sticky="e")
    Label(frame, text="Mines:").grid(row=3, pady=5, sticky="e")

    eRow = Entry(frame)
    eCol = Entry(frame)
    eMine = Entry(frame)

    eRow.insert(10, "10")
    eCol.insert(10, "10")
    eMine.insert(10, "10")

    eRow.grid(column=1, row=1, padx=10, pady=5, sticky="e")
    eCol.grid(column=1, row=2, padx=10, pady=5, sticky="e")
    eMine.grid(column=1, row=3, padx=10, pady=5, sticky="e")



    def start():
        try:
            global x, y, m
            y = int(eRow.get())
            x = int(eCol.get())
            m = int(eMine.get())
            if m > x * y or x < 0 or y < 0 or m < 0 or x > 40 or y > 20:
                raise Exception
            window.destroy()
        except:
            Label(frame, text="Enter a valid input!", fg="red").grid(row=6)
            return

    def quitGame():
        window.destroy()
        exit(None)

    Button(frame, text="Start", command=lambda:start()).grid(sticky="ne", row=4, column=1)
    Button(frame, text="Quit", command=lambda:quitGame()).grid(sticky="nw", row=4, column=0)

    print("Game ready!")

    window.mainloop()
    window = Tk()
    window.resizable(False, False)
    window.title("Minesweeper")
    return [x,y], m, window


# Ritar brädet på skärmen
def draw(board: list, window: Tk):

    def restart():
        window.destroy()
        main()
        window.quit()

    frm = ttk.Frame(window, padding=10)
    frm.grid()
    for y in range(len(board)):
        for x in range(len(board[0])):
            board[y][x].getTile(frm)

    print(".")

    frm2 = ttk.Frame(window, padding=10)
    frm2.grid()
    Button(frm2, text="Quit", command=lambda:exit(None)).grid(row=0,column=0, padx=10)
    Button(frm2, text="Restart", command=restart).grid(row=0,column=1, padx=10)
    print("Ready to blow you up!")
    startingTime = datetime.now()
    print(startingTime)
    for y in range(len(board)):
        for x in range(len(board[0])):
            board[y][x].startingTime(startingTime)

    window.mainloop()

main()