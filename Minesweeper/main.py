from box import Box
import random
from tkinter import *
from tkinter import ttk

# Huvudfunktion för att köra programmet
def main():
    size, mineCount = defInitials()
    board = []
    for y in range(size[1]):
        row = []
        for x in range(size[0]):
            row.append(Box())
        board.append(row)
    
    mines = random.sample(range(len(board[0])*len(board)), mineCount)
    for i in mines:
        y = int(i/len(board[0]))
        x = i%len(board[0])
        board[x][y].setMine()

    draw(board)



# Definierar initialvärden för brädesstorlek och antalet minor
def defInitials():
    while True:
        try:
            x = int(input("Enter board size (A x B)\nA: "))
            y = int(input("B: "))
            mineCount = int(input("Enter mine count: "))
            if mineCount > x * y or x < 0 or y < 0 or mineCount < 0:
                raise Exception
            break
        except:
            print("---\nEnter a valid input\n---")
    return [x,y], mineCount

# Ritar brädet på skärmen
def draw(board: list):
    """
    for y in range(len(board)):
        for x in range(len(board[0])):
            print(board[x][y], end="")
        print()
    """
    window = Tk()
    frm = ttk.Frame(window, padding=10)
    frm.grid()
    for y in range(len(board)):
        for x in range(len(board[0])):
            box = ttk.Button(frm, text=board[x][y], command=lambda : board[x][y].open())
            box.grid(column=x, row=y)
            """frame = ttk.Frame(frm, text=board[x][y], width=50, height=50)
            frame.grid(column=x, row=y)
            frame.grid_propagate(False) #disables resizing of frame
            frame.columnconfigure(0, weight=1) #enables button to fill frame
            frame.rowconfigure(0,weight=1) #any positive number would do the trick

            btn = ttk.Button(frame)
            btn.grid(sticky="nswe")"""
    window.mainloop()

main()