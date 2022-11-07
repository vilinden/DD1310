from numpy import arange
import math


lightDic = {
    0 : "M",
    0.3  : "*",
    0.5 : "+",
    0.7 : "-",
    0.9 : ".",
    1 : " "
}

r = int(input("R: "))
x0 = int(input("x0: "))
y0 = int(input("y0: "))

z0 = math.sqrt(math.pow(r,2)-math.pow(x0,2)-math.pow(y0,2))

for y in range(-r, r):
    for x in range(-r, r):
        try:
            z = math.sqrt(math.pow(r,2)-math.pow(x,2)-math.pow(y,2))
            b = (x*x0 + y*y0 + z*z0)/r**2
        except:
            b = 0
        
        if b > 0.9:
            print(lightDic[1], end="")
        elif b > 0.7:
            print(lightDic[0.9], end="")
        elif b > 0.5:
            print(lightDic[0.7], end="")
        elif b > 0.3:
            print(lightDic[0.5], end="")
        elif b > 0:
            print(lightDic[0.3], end="")
        else:
            print(lightDic[0],end="")
    print()