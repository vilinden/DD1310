# 2022-10-04
# Viktor Lindén, Erik Stare

from glosa import Glosa

# Presenterar programmet för användaren. Skriver ut vad som förväntas av användaren. 
# Används för att göra programmet mer estetiskt snyggt.
def presentaion():
    print("Detta är ett glosförhör. Skriv rätt översättning till engelska utifrån det svenska ord som presenteras.\n")

# Uppdaterar textfilen med rätt/fel svar
def spara(filväg, glosor):
    tillFil = ""
    for i in range(len(glosor)):
        tillFil += "{}:{}:{}:{}\n".format(glosor[i].getSvenska(), glosor[i].getEngelska(), glosor[i].getRätt(), glosor[i].getFel())
    
    f = open(filväg, "w")
    f.write(tillFil)
    f.close()

# Ber användaren översätta det svenska ordet till engelska, antalet försök går att välja med parameter 3. 
# Returnerar rätt eller fel.
def översättEttOrd(glosa):
    inmatning = input("Vad är {} på engelska? ".format(glosa.getSvenska()))
    if inmatning.lower() == glosa.getEngelska().lower():
        print("Bravo!")
        glosa.addCorrect()
        return 1
    else:
        glosa.addWrong()
        print("Det var tyävrr fel! Rätt svar är "+ glosa.getEngelska())
    return 0

# Läser given textfil och gör till glosobjekt
def läsTextfilTillGlosor(filväg):
    try:
        svenska, engelska, rätt, fel, glosObj = ([] for i in range(5))
        fil = open(filväg, "r")
        lista = fil.readlines()
        for i in range(len(lista)):
            lista[i] = lista[i].replace("\n", "")
            glosa = lista[i].split(":")
            svenska.append(glosa[0])
            engelska.append(glosa[1])
            rätt.append(int(glosa[2]))
            fel.append(int(glosa[3]))
        fil.close()

        for i in range(len(svenska)):
            glosObj.append(Glosa(svenska[i], engelska[i], rätt[i], fel[i]))

        return glosObj

    except Exception as err:
        print("ERROR: " + str(err))
        return []
    

# Loopar igenom alla ord och skickar tillbaka resultatet på glosförhöret
def glosförhör():
    # Etablerar variabel för att hålla koll på antalet rätta översättningar.
    resultat = 0
    filväg = "glosor.txt"

    glosor = läsTextfilTillGlosor(filväg)

    # Loopar igenom varje index för den svenska listan
    for i in range(len(glosor)):
        resultat += översättEttOrd(glosor[i])

    print("Du fick {} rätt och {} fel".format(resultat, len(glosor) - resultat))
    print("{:<10}{:<10}{:<8}{}".format("Svenska", "Engelska", "Senaste", "Rätt/Tot"))
    for glosa in glosor:
        print(glosa)
    
    spara(filväg, glosor)

# Kör programmet
def main():    
    presentaion()

    glosförhör()


main()