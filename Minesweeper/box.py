from tkinter import *
from tkinter import ttk

class Box:
    def __init__(self,x,y,window):
        self.__nearby = 0
        self.__nearbyBoxes = []
        self.__mine = False
        self.__flagged = False
        self.__open = False
        self.x = x
        self.y = y
        self.window = window
        self.img = PhotoImage(file = f"blank.png")
        self.checkingWin = False
        self.__gameOverDone = False

    def __str__(self):
        if self.__open:
            if self.__mine:
                return "X"
            else: return str(self.__nearby)
        else: return ""


    def setNearbyBoxes(self, boxes: list):
        self.__nearbyBoxes = boxes

    def setMine(self):
        self.__mine = True
        self.__nearby = "bomb"
    def getMine(self):
        return self.__mine

    def setNearby(self, nearby: int):
        self.__nearby = nearby
    def getNearby(self):
        return self.__nearby

    def setFlagged(self):
        if not self.isOpen():
            self.__flagged = not self.__flagged
            if self.__flagged:
                self.img = PhotoImage(file = f"flag.png")
                self.label.config(image=self.img)
            else:
                self.img = PhotoImage(file = f"blank.png")
                self.label.config(image=self.img)
            
            winList = self.recursiveWinCheckFlags()
            if not False in winList:
                self.win()
            else:
                self.resetWinCheck()


    def getFlagged(self):
        return self.__flagged


    def getBox(self, frame):
        self.label = Label(frame, image=self.img)
        self.label.grid(column = self.x, row = self.y)
        self.label.bind("<Button-1>", lambda a:self.open())
        self.label.bind("<Button-2>", lambda a:self.setFlagged())
        self.label.bind("<Button-3>", lambda a:self.setFlagged())
        return self.label

    def open(self):
        if not self.__open:
            if not self.__mine:
                self.__open = True
                self.img = PhotoImage(file = f"{self.__nearby}.png")
                self.label.config(image=self.img)
                if self.__nearby == 0:
                    for box in self.__nearbyBoxes:
                        box.open()
                
                winList = self.recursiveWinCheckBlanks()
                if not False in winList:
                    self.win()
                else:
                    self.resetWinCheck()

            else:
                self.gameOver()
        

    def isOpen(self):
        return self.__open

    def gameOver(self):
        if not self.__gameOverDone:
            if not self.isOpen():
                if self.__mine:
                    self.img = PhotoImage(file = "bomb.png")
                    self.label.config(image=self.img)
                else:
                    self.open()
            self.__gameOverDone = True
            for next in self.__nearbyBoxes:
                next.gameOver()

    def recursiveWinCheckFlags(self):
        self.checkingWin = True
        recReturn = []
        if self.__mine == True:
            if self.__flagged == False:
                recReturn.append(False)
                return recReturn

        if self.__mine == False:
            if self.__flagged == True:
                recReturn.append(False)
                return recReturn
        for n in self.__nearbyBoxes:
                if self.__mine and self.__flagged: recReturn.append(True)
                if not n.checkingWin:
                    for ret in n.recursiveWinCheckFlags():
                        recReturn.append(ret)

        return recReturn

    def recursiveWinCheckBlanks(self):
        self.checkingWin = True
        recReturn = []
        if self.__open == False and self.__mine == False:
            recReturn.append(False)
            return recReturn

        for n in self.__nearbyBoxes:
                if self.__mine == False and self.__open: recReturn.append(True)
                if not n.checkingWin:
                    for ret in n.recursiveWinCheckBlanks():
                        if ret is list:
                            return recReturn.extend(ret)
                        else:
                            recReturn.append(ret)

        return recReturn

    def resetWinCheck(self):
        self.checkingWin = False
        for n in self.__nearbyBoxes:
            if n.checkingWin:
                n.resetWinCheck()

    def win(self):
        self.gameOver()
        winScreen = Tk()
        winScreen.title("You Won!")

        frame = Frame(winScreen, padx=50, pady=50, background="green")
        frame.pack()

        quitBtn = Button(frame, text="Quit", command=lambda:exit(None))
        restartBtn = Button(frame, text="New Game", command=lambda:winScreen.quit())

        restartBtn.grid(row=1, column=0)
        quitBtn.grid(row=1, column=1)

        label = Label(frame, text="Congratulations! You won!", background="green", pady=30)
        label.grid(row=0, columnspan=2)

        winScreen.mainloop()
        print("Restarting game...")
        winScreen.destroy()
        self.window.destroy()