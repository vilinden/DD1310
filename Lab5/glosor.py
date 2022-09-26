# 2022-09-21
# Viktor Lindén, Erik Stare

import glosa

# Presenterar programmet för användaren. Skriver ut vad som förväntas av användaren. 
# Används för att göra programmet mer estetiskt snyggt.
def presentaion():
    print("Detta är ett glosförhör. Skriv rätt översättning till engelska utifrån det svenska ord som presenteras.\n")

# Ber användaren översätta det svenska ordet till engelska, antalet försök går att välja med parameter 3. Returnerar rätt eller fel.
def översättEttOrd(glosa):
    inmatning = input("Vad är {} på engelska? ".format(glosa.svenska))
    if inmatning.lower() == glosa.engelska.lower():
        print("Bravo!")
        return 1 
    else:
        print("Det var tyävrr fel! Rätt svar är "+ glosa.engelska)
    return 0

# Läser given textfil
def läsTextfilTillLista(filväg):
    try:
        svenska = []
        engelska = []
        fil = open(filväg, "r")
        lista = fil.readlines()
        for i in range(len(lista)):
            lista[i] = lista[i].replace("\n", "")
            glosa = lista[i].split(":")
            svenska.append(glosa[0])
            engelska.append(glosa[1])
        fil.close()
        return svenska, engelska
    except:
        return []

# Tar emot listor med glosor och gör till glosobjekt.add()
def listaTillGlosa(svenska, engelska):
    glosObj = []
    for i in range(len(svenska)):
        glosObj.append(glosa(svenska[i], engelska[i]))
    return glosObj

# Loopar igenom alla ord och skickar tillbaka resultatet på glosförhöret
def glosförhör():
    # Etablerar variabel för att hålla koll på antalet rätta översättningar.
    resultat = 0

    svenskaStr, engelskaStr = läsTextfilTillLista("glosor.txt")
    glosor = listaTillGlosa(svenskaStr, engelskaStr)

    # Loopar igenom varje index för den svenska listan
    for i in range(len(glosor)):
        resultat += översättEttOrd(glosor[i])

    return resultat, len(glosor) - resultat

# Kör programmet
def main():    
    presentaion()

    rätt, fel = glosförhör()

    # Resultatet presenteras för användaren med antalet rätta samt felaktiga svar.
    print("\nDu hade {} rätt och {} fel".format(rätt, fel))


main()