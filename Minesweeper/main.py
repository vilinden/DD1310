from typing import List
from box import Box
import random

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

def draw(board: list):
    for y in range(len(board)):
        for x in range(len(board[0])):
            print(board[x][y], end="")
        print()

main()