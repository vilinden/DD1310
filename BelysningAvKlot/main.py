import math
from time import sleep
from tkinter import *

def draw(x0, y0, window):   
    for y in range(-r, r):
        rowList = list()
        for x in range(-r, r):
            try:
                z = math.sqrt(math.pow(r,2)-math.pow(x,2)-math.pow(y,2))
                b = (x*x0 + y*y0 + z*z0)/r**2
            except:
                b = 0
            
            if math.pow(r,2)-math.pow(x,2)-math.pow(y,2) < 0:
                b = -1
            else:
                b = round(b, 1)
                if b > 1: b=1
                elif b < -1: b=-1
            t = lightDic[b]

            rowList.append(canvas.create_rectangle((x+r+0.5)*cellSize, (y+r+0.5)*cellSize, (x+r+0.5)*cellSize+cellSize, (y+r+0.5)*cellSize+cellSize, fill=t))
        canList.append(rowList)
    canvas.pack()

lightDic = {
    -1 : "#09aff1",
    -0.9 : "#000000",
    -0.8 : "#010101",
    -0.7 : "#020202",
    -0.6 : "#040404",
    -0.5 : "#060606",
    -0.4 : "#080808",
    -0.3 : "#0A0A0A",
    -0.2 : "#0C0C0C",
    -0.1 : "#0F0F0F",
    0 : "#111111",
    0.1 : "#222222",
    0.2 : "#333333",
    0.3  : "#444444",
    0.4  : "#666666",
    0.5 : "#777777",
    0.6 : "#999999",
    0.7 : "#AAAAAA",
    0.8 : "#BBBBBB",
    0.9 : "#CCCCCC",
    1 : "#FFFFFF"
}
cellSize = 12
canList = list()

r = int(input("R: "))
x0 = 0
y0 = 0

z0 = math.sqrt(math.pow(r,2)-math.pow(x0,2)-math.pow(y0,2))

window = Tk()

canvas = Canvas(window, width=cellSize*r*2, height=cellSize*r*2)

draw(x0, y0, window)

wx = Scale(window, from_=-r, to=r)
wx.pack()

wy = Scale(window, from_=-r, to=r, orient=HORIZONTAL)
wy.pack()


def updateLight():
    for y in range(-r, r):
        for x in range(-r, r):
            x0 = int(wx.get())
            y0 = int(wy.get())
            try:
                z = math.sqrt(math.pow(r,2)-math.pow(x,2)-math.pow(y,2))
                b = (x*x0 + y*y0 + z*z0)/r**2
            except:
                b = 0
            
            if math.pow(r,2)-math.pow(x,2)-math.pow(y,2) < 0:
                b = -1
            else:
                b = round(b, 1)
                if b > 1: b=1
                elif b < -1: b=-1
            t = lightDic[b]

            canvas.itemconfig(canList[x+r][y+r], fill=t)
    window.after(100, updateLight)

updateLight()
window.mainloop()    