from tkinter import *
from tkinter import ttk
from datetime import datetime

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
        self.img = PhotoImage(file = f"img/blank.png")
        self.checkingWin = False
        self.__gameOverDone = False

    def __str__(self):
        if self.__open:
            if self.__mine:
                return "X"
            else: return str(self.__nearby)
        else: return ""

    def setTotalMines(self, mines: int):
        self.__totalMines = mines

    def startingTime(self, time):
        self.__startTime = time

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

    def setFlagged(self, isFirst = False):
        if not self.isOpen():
            self.__flagged = not self.__flagged
            if self.__flagged:
                self.img = PhotoImage(file = f"img/flag.png")
                self.label.config(image=self.img)
            else:
                self.img = PhotoImage(file = f"img/blank.png")
                self.label.config(image=self.img)
            
            if isFirst:
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
        self.label.bind("<Button-1>", lambda a:self.open(True))
        self.label.bind("<Button-2>", lambda a:self.setFlagged(True))
        self.label.bind("<Button-3>", lambda a:self.setFlagged(True))
        return self.label

    def open(self, isFirst = False):
        if not self.__open:
            if not self.__mine:
                self.__open = True
                self.img = PhotoImage(file = f"img/{self.__nearby}.png")
                self.label.config(image=self.img)
                if self.__nearby == 0:
                    for box in self.__nearbyBoxes:
                        box.open()
                if isFirst:
                    winList = self.recursiveWinCheckBlanks()
                    if not False in winList:
                        self.win()
                    else:
                        self.resetWinCheck()

            else:
                self.loose()
        

    def isOpen(self):
        return self.__open

    def gameOver(self):
        if not self.__gameOverDone:
            if not self.isOpen():
                if self.__mine:
                    self.img = PhotoImage(file = "img/bomb.png")
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
        gameLengthTime = datetime.now() - self.__startTime
        seconds = gameLengthTime.total_seconds()

        score = self.__totalMines * 100 / seconds

        hours = int(seconds / 3600)
        seconds = seconds - hours*3600
        minutes = int(seconds / 60)
        seconds = seconds - minutes*60

        def save():
            try:
                name = str(nameEntry.get())
                if len(name) < 1 or len(name) > 15:
                    raise
                f = open("top10.txt", "r")
                unformattedTopList = f.readlines()
                f.close
                topList=[]
                for i in range(len(unformattedTopList)):
                    topList.append([unformattedTopList[i].split(":")[0], float(unformattedTopList[i].split(":")[1])])
                scores = []
                for i in range(len(topList)):
                    scores.append(float(topList[i][1]))
                if len(scores) < 10:
                    topList.append([name, score])

                topList = sorted(topList, key=lambda list: list[1])

                f = open("top10.txt", "w")
                writtingList = []
                for i in range(len(topList)):
                    writtingList.append(f"{topList[i][0]}:{topList[i][1]}\n")
                f.writelines(writtingList[::-1])
                f.close()
                saveNameBtn.config(state='disabled', text="Saved!")
                try: 
                    winScreen.nametowidget("failedToSave").destroy()
                except: pass

            except Exception as err:
                try: winScreen.nametowidget("failedToSave")
                except: Label(winScreen, text="Failed to save score!", fg="red", name="failedToSave").pack()

        def showTop10():
            top10Window = Tk()
            f = open("top10.txt", "r")
            unformattedTopList = f.readlines()
            f.close

            tableDic = {
                0:"gold",
                1:"silver",
                2:"chocolate1"
            }

            for i in range(len(unformattedTopList)):
                Label(top10Window, text=f"{i+1}:", bg=tableDic.get(i, top10Window.cget('bg'))).grid(row=i, sticky="nw", padx=5, pady=10)
                Label(top10Window, text=f'{unformattedTopList[i].split(":")[0]}').grid(row=i, column=1,sticky="nw", pady=10)
                Label(top10Window, text=f'{float(unformattedTopList[i].split(":")[1]):.2f}').grid(row=i, column=2,sticky="ne", padx=10, pady=10)

        self.gameOver()
        winScreen = Tk()
        winScreen.title("You Won!")

        frame = Frame(winScreen, padx=50, pady=50, background="lightgreen")
        frame.pack()

        quitBtn = Button(frame, text="Quit", command=lambda:exit(None))
        restartBtn = Button(frame, text="New Game", command=lambda:winScreen.quit())

        restartBtn.grid(row=3, column=0, sticky="w")
        quitBtn.grid(row=3, column=2, sticky="ne")

        label = Label(frame, text="Congratulations! You won!\nThe game took {} hours, {} minutes and {:.2f} seconds!".format(hours, minutes, seconds), background="lightgreen", pady=30)
        label.grid(row=0, columnspan=3)

        nameEntry = Entry(frame)
        nameLabel = Label(frame, text="Enter name to save:", background="lightgreen", pady=10)
        saveNameBtn = Button(frame, text="Save", command=lambda:save())
        showTop10Btn = Button(frame, text="Show top 10", command=lambda:showTop10())
        nameEntry.grid(row=1, column=1)
        nameLabel.grid(row=1, column=0)
        saveNameBtn.grid(row=1, column=2, sticky="e")
        showTop10Btn.grid(row=2, column=2, sticky="ne", pady=15)


        winScreen.mainloop()
        print("Restarting game...")
        winScreen.destroy()
        self.window.destroy()

    def loose(self):
        gameLengthTime = datetime.now() - self.__startTime
        seconds = gameLengthTime.total_seconds()
        hours = int(seconds / 3600)
        seconds = seconds - hours*3600
        minutes = int(seconds / 60)
        seconds = seconds - minutes*60

        self.gameOver()
        self.img = PhotoImage(file="img/explode.png")
        self.label.config(image=self.img)
        winScreen = Tk()
        winScreen.title("You Lost!")

        frame = Frame(winScreen, padx=50, pady=50, background="pink")
        frame.pack()

        quitBtn = Button(frame, text="Quit", command=lambda:exit(None))
        restartBtn = Button(frame, text="New Game", command=lambda:winScreen.quit())

        restartBtn.grid(row=1, column=0)
        quitBtn.grid(row=1, column=1)

        label = Label(frame, text="You Lost!\nThe game took {} hours, {} minutes and {:.2f} seconds!\nLet's try again!".format(hours, minutes, seconds), background="pink", pady=30)
        label.grid(row=0, columnspan=2)

        winScreen.mainloop()
        print("Restarting game...")
        winScreen.destroy()
        self.window.destroy()