from box import Box
import random
from tkinter import *
from tkinter import ttk
from functools import partial

# Huvudfunktion för att köra programmet
def main():
    window = Tk()
    size, mineCount, window = defInitials(window)
    board = []
    for y in range(size[1]):
        row = []
        for x in range(size[0]):
            row.append(Box(x,y,window))
        board.append(row)
    
    mines = random.sample(range(len(board[0])*len(board)), mineCount)
    for i in mines:
        y = int(i/len(board[0]))
        x = i%len(board[0])
        board[x][y].setMine()

    for row in board:
        for tile in row:
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
            tile.setNearbyBoxes(neighbors)




    draw(board,window)



# Definierar initialvärden för brädesstorlek och antalet minor
def defInitials(window):
    x = 10
    y = 10
    mineCount = 6
    while True:
        try:
            frame = ttk.Frame(window, padding=0)
            frame.grid(pady=10)
            Label(frame, text="Rows:").grid(row=1, padx=10, pady=5)
            Label(frame, text="Columns:").grid(row=2, padx=10, pady=5)
            Label(frame, text="Mines:").grid(row=3, padx=10, pady=5)

            eRow = Entry(frame)
            eCol = Entry(frame)
            eMine = Entry(frame)

            eRow.insert(10, str(x))
            eCol.insert(10, str(y))
            eMine.insert(10, str(mineCount))

            eRow.grid(column=1, row=1, padx=10, pady=5, sticky="w")
            eCol.grid(column=1, row=2, padx=10, pady=5, sticky="w")
            eMine.grid(column=1, row=3, padx=10, pady=5, sticky="w")



            def start():
                x = int(eRow.get())
                y = int(eCol.get())
                mineCount = int(eMine.get())
                if mineCount > x * y or x < 0 or y < 0 or mineCount < 0:
                    raise Exception
                window.destroy()

            Button(frame, text="Start", command=start).grid(sticky="n", columnspan=2)

            window.mainloop()
        except:
            print("---\nEnter a valid input\n---")
        finally:
            window = Tk()
            break
    return [x,y], mineCount, window


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
            board[y][x].getBox(frm)

    frm2 = ttk.Frame(window, padding=10)
    frm2.grid()
    Button(frm2, text="Quit", command=lambda:window.quit()).grid(row=0,column=0, padx=10)
    Button(frm2, text="Restart", command=restart).grid(row=0,column=1, padx=10)
    window.mainloop()

main()