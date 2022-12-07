from classes import *

def main():
    width, height, bombs = getBoardSettings()
    board = Board(width, height, bombs)
    gui = GUI()
    gui.input("Width:", 10)
    gui.input("Height:", 10)
    gui.input("Bombs:", 5)
    gui.button()
    gui.update()

def getBoardSettings():
    width = int(input("Width of board: "))
    height = int(input("Height of board: "))
    bombs = int(input("Numbers of bombs: "))
    return width, height, bombs

if __name__ == "__main__":
    main()