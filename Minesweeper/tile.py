from tkinter import *
from datetime import datetime

# Klass för rutor
class Tile:
    # Initiferar ett Tile-objekt
    def __init__(self,x,y,window):
        self.__nearby = 0
        self.__nearbyTiles = []
        self.__mine = False
        self.__flagged = False
        self.__open = False
        self.x = x
        self.y = y
        self.__window = window
        self.__img = PhotoImage(file = f"img/blank.png")
        self.checkingWin = False
        self.__gameOverDone = False

    # Setter totala antalet minor på brädet till attributet för att kunna räkna poäng i slutet
    def setTotalMines(self, mines: int):
        self.__totalMines = mines

    # Sätter starttiden då spelet började
    def startingTime(self, time):
        self.__startTime = time

    # Sätter en lista över angränsande rutor
    def setNearbyTiles(self, tiles: list):
        self.__nearbyTiles = tiles

    # Sätter rutan till en mina
    def setMine(self):
        self.__mine = True
        self.__nearby = "bomb"
    # Returnerar boolesk beroende på om rutan är en mina
    def getMine(self):
        return self.__mine

    # Sätter hur många minor som angränsar till rutan.
    def setNearby(self, nearby: int):
        self.__nearby = nearby
    def getNearby(self):
        return self.__nearby

    # Markerar rutan som flaggad. isFirst är viktigt för att kontrollen om vinst algoritmen ska
    # kunna köras någotlunda effektivt.
    def setFlagged(self, isFirst = False):
        if not self.isOpen():
            self.__flagged = not self.__flagged
            if self.__flagged:
                self.__img = PhotoImage(file = f"img/flag.png")
                self.label.config(image=self.__img)
            else:
                self.__img = PhotoImage(file = f"img/blank.png")
                self.label.config(image=self.__img)
            
            if isFirst:
                winList = self.recursiveWinCheckFlags()
                if not False in winList:
                    self.win()
                else:
                    self.resetWinCheck()

    # Returnerar boolesk om rutan är flaggad av användaren
    def getFlagged(self):
        return self.__flagged

    # Returnerar tkinter-label för denna ruta
    def getTile(self, frame):
        self.label = Label(frame, image=self.__img)
        self.label.grid(column = self.x, row = self.y)
        self.label.bind("<Button-1>", lambda a:self.open(True))
        self.label.bind("<Button-2>", lambda a:self.setFlagged(True))
        self.label.bind("<Button-3>", lambda a:self.setFlagged(True))
        return self.label

    # Hanterar användarens klick på rutan
    def open(self, isFirst = False):
        if not self.__open:
            if not self.__mine:
                self.__open = True
                self.__img = PhotoImage(file = f"img/{self.__nearby}.png")
                self.label.config(image=self.__img)
                if self.__nearby == 0:
                    for tile in self.__nearbyTiles:
                        tile.open()
                if isFirst:
                    winList = self.recursiveWinCheckBlanks()
                    if not False in winList:
                        self.win()
                    else:
                        self.resetWinCheck()

            else:
                self.loose()
        
    # Returnerar boolesk om rutan är öppen eller ej
    def isOpen(self):
        return self.__open

    # Hanterar spelplanen när spelet är över (Visar alla minor)
    def gameOver(self):
        if not self.__gameOverDone:
            if not self.isOpen():
                if self.__mine:
                    self.__img = PhotoImage(file = "img/bomb.png")
                    self.label.config(image=self.__img)
                else:
                    self.open()
            self.__gameOverDone = True
            for next in self.__nearbyTiles:
                next.gameOver()

    # Går rekursivt igenom spelbrädet och kollar om alla minor och endast minor är flaggade => Vinst
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
        for n in self.__nearbyTiles:
                if self.__mine and self.__flagged: recReturn.append(True)
                if not n.checkingWin:
                    for ret in n.recursiveWinCheckFlags():
                        recReturn.append(ret)

        return recReturn

    # Går rekursivt igenom spelbrädet och kollar om alla icke-minor är öppnade => Vinst
    def recursiveWinCheckBlanks(self):
        self.checkingWin = True
        recReturn = []
        if self.__open == False and self.__mine == False:
            recReturn.append(False)
            return recReturn

        for n in self.__nearbyTiles:
                if self.__mine == False and self.__open: recReturn.append(True)
                if not n.checkingWin:
                    for ret in n.recursiveWinCheckBlanks():
                        if ret is list:
                            return recReturn.extend(ret)
                        else:
                            recReturn.append(ret)

        return recReturn

    # Återställer attributet checkingWin för alla rutor rekursivt
    def resetWinCheck(self):
        self.checkingWin = False
        for n in self.__nearbyTiles:
            if n.checkingWin:
                n.resetWinCheck()

    # Hanterar vinst
    def win(self):
        gameLengthTime = datetime.now() - self.__startTime
        seconds = gameLengthTime.total_seconds()

        score = self.__totalMines * 1000 / (seconds + 100)

        hours = int(seconds / 3600)
        seconds = seconds - hours*3600
        minutes = int(seconds / 60)
        seconds = seconds - minutes*60

        # Sparar resultatet i top10lista
        def save():
            try:
                name = str(nameEntry.get())
                if len(name) < 1 or len(name) > 15:
                    raise
                try:
                    f = open("top10.txt", "r", encoding="ASCII")
                except:
                    f = open("top10.txt", "w+")
                    f.close
                    f = open("top10.txt", "r", encoding="ASCII")

                unformattedTopList = f.readlines()
                f.close
                topList=[]
                for i in range(len(unformattedTopList)):
                    topList.append([unformattedTopList[i].split(":")[0], float(unformattedTopList[i].split(":")[1])])
                scores = []
                for i in range(len(topList)):
                    scores.append(float(topList[i][1]))

                topList.append([name, score])

                topList = sorted(topList, key=lambda list: list[1])[::-1]
                f = open("top10.txt", "w")
                writtingList = []
                if len(topList) > 10:
                    for i in range(10):
                        writtingList.append(f"{topList[i][0]}:{topList[i][1]}\n")
                else:
                    for i in range(len(topList)):
                        writtingList.append(f"{topList[i][0]}:{topList[i][1]}\n")

                f.writelines(writtingList)
                f.close()
                saveNameBtn.config(state='disabled', text="Saved!")
                try: 
                    winScreen.nametowidget("failedToSave").destroy()
                except: pass

            except Exception as err:
                try: winScreen.nametowidget("failedToSave")
                except: print(err); Label(winScreen, text="Failed to save score!", fg="red", name="failedToSave").pack()

        # Ritar ut top10listan med tkinter
        def showTop10():
            top10Window = Tk("Top 10")
            try:
                f = open("top10.txt", "r")
                unformattedTopList = f.readlines()
                f.close
            except:
                f = open("top10.txt", "w+")
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

        label = Label(frame, text="Congratulations! You won!\nThe game took {} hours, {} minutes and {:.2f} seconds!\nThis gives you a score of {:.2f}!".format(hours, minutes, seconds, score), background="lightgreen", pady=30)
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
        self.__window.destroy()

    # Hanterar förlust
    def loose(self):
        gameLengthTime = datetime.now() - self.__startTime
        seconds = gameLengthTime.total_seconds()
        hours = int(seconds / 3600)
        seconds = seconds - hours*3600
        minutes = int(seconds / 60)
        seconds = seconds - minutes*60

        self.gameOver()
        self.__img = PhotoImage(file="img/explode.png")
        self.label.config(image=self.__img)
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
        self.__window.destroy()