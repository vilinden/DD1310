import os
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
        self.__done = False

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
        self.__flagged = not self.__flagged
        if self.__flagged:
            self.img = PhotoImage(file = f"flag.png")
            self.label.config(image=self.img)
        else:
            self.img = PhotoImage(file = f"blank.png")
            self.label.config(image=self.img)

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
            else:
                self.gameOver()

    def isOpen(self):
        return self.__open

    def gameOver(self):
        if not self.__done:
            if not self.isOpen():
                if self.__mine:
                    self.img = PhotoImage(file = "bomb.png")
                    self.label.config(image=self.img)
            self.__done = True
            for next in self.__nearbyBoxes:
                next.gameOver()