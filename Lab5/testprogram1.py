#Testprogram 1 laboration 5
#Det är lämpligt att kommentera bort huvudprogramkod som ni kan ha i
#modulen Kurs (filen Kurs.py)
try:
    from Kurs import Kurs
except ModuleNotFoundError:
    print("Filen ligger i fel katalog eller så är inte er pythonfil döpt till Kurs.py")
    exit()
    

#Skapar ett objekt och kollar att klassen heter rätt
try:
    testobjekt=Kurs("PrgE",6)
except NameError:
    print("Er klass heter inte Kurs")
    exit()


#Kollar att attributen heter rätt och innehåller rätt information
try:
    if testobjekt.namn=="PrgE":
        print("namn lagrat korrekt")
    else:
        print("namns värde matchar inte inskickat värde :(")
    if testobjekt.poäng==6:
        print("poängattributet har korrekt värde")
    else:
        print("poängattribbutet matchar inte inskickat värde :(")
    if testobjekt.avklarad==False:
        print("Attributet avklarad har fått korrekt startvärde")
    else:
        print("Attributet avklarad fick inte korrekt startvärde :(")
    print("Testet slutfört, alla attribut finns :)")
except AttributeError:
    print("Ett eller flera attribut verkar ha fel namn (kan vara ett åäö-prblem också)")

    
