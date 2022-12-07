from classes import *

class Program:
    def main(self):
        self.gui = GUI()
        while True:    
            self.boardWidth, self.boardHeight, self.amountOfBombs = 0,0,0
            try:
                self.getBoardSettings()
                break
            except:
                self.gui.newWindow

        self.board = Board(self.boardWidth, self.boardHeight, self.amountOfBombs)
        for row in self.board.get_matrix():
            for tile in row:
                print(tile, end=" ")
            print()

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

if __name__ == "__main__":
    program = Program()
    program.main()