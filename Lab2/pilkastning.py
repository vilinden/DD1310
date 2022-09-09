#2022-09-01
#Viktor Lindén, Erik Stare
namn1=input("Vad heter kastare 1") 
namn2=input("Vad heter kastare 2") 
poang1=[] 
poang2=[] 
for i in range(5): 
    poang=int(input("Vilken poäng fick "+namn1+" på kast nr "+str(i+1))) 
    poang1.append(poang) 
for i in range(5): 
    poang2.append(int(input("Vilken poäng fick "+namn2+" på kast nr "+str(i+1))))

# Variabler för att kunna addera poängen till en total summa.
poang1_ = 0
poang2_ = 0

# För varje element i poang1 och poang2, addera till de tidigare variablerna till en summa.
for i in range(len(poang1)):
    poang1_ += poang1[i]
    poang2_ += poang2[i]

# Printar ut vinnaren och resultaten till användaren.
print("Grattis " + namn1 + ", du vann med " + str(poang1_) + " poäng mot "+ namn2 + " som fick " + str(poang2_) + " poäng!") if poang1_ > poang2_ else print("Grattis " + namn2 + ", du vann med " + str(poang2_) + " poäng mot "+ namn1 + " som fick " + str(poang1_) + " poäng!")