#Testprogram 2 laboration 5
#Det är lämpligt att kommentera bort huvudprogramkod som ni kan ha i
#modulen Kurs (filen Kurs.py)
from Kurs import Kurs
testobjekt=Kurs("PrgE", 7.5)
testobjekt.avklarad=True
print("testar\n"+str(testobjekt))
text=str(testobjekt)
if "PrgE" in text:
    print("Kursnamn verkar finnas med")
else:
    print("Kursnamn verkar saknas")
if str(7.5) in text:
    print("hp verkar finnas med")
else:
    print("hp verkar saknas")
if str(True) in text:
    print("avklarad verkar finnas med")
else:
    print("avklarad verkar saknas")