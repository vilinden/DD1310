# 2022-09-21
# Viktor Lindén, Erik Stare

# Presenterar programmet för användaren. Skriver ut vad som förväntas av användaren. \n används för att göra programmet mer estetiskt snyggt.
from turtle import right


def presentaion():
    print("Detta är ett glosförhör. Skriv rätt översättning till engelska utifrån det svenska ord som presenteras.\n")

# Ber användaren översätta det svenska ordet till engelska, antalet försök går att välja med parameter 3. Returnerar rätt eller fel.
def översättEttOrd(svenska, engelska, försök = 1):
    inmatning = input("Vad är {} på engelska? ".format(svenska))
    if inmatning.lower() == engelska.lower():
        print("Bravo!")
        return 1
    elif försök == 1:
        print("Det var tyävrr fel! Rätt svar är "+ engelska)
    else:
        print("Det var tyvärr fel, försök igen!")
    return 0

# Läser given textfil
def läsTextfilTillLista(filväg):
    try:
        svenska = []
        engelska = []
        svårighet = []
        fil = open(filväg, "r")
        lista = fil.readlines()
        for i in range(len(lista)):
            lista[i] = lista[i].replace("\n", "")
            glosa = lista[i].split(":")
            svenska.append(glosa[0])
            engelska.append(glosa[1])
            svårighet.append(int(glosa[2]))
        fil.close()
        return svenska, engelska, svårighet
    except:
        return []

# Loopar igenom alla ord och skickar tillbaka resultatet på glosförhöret
def glosförhör():
    # Etablerar variabel för att hålla koll på antalet rätta översättningar.
    resultat = 0

    svenska, engelska, svårighet = läsTextfilTillLista("glosor.txt")

    # Loopar igenom varje index för den svenska listan
    for i in range(len(svenska)):
        resultatTemp = 0
        for försök in range(svårighet[i], 0, -1):
            resultatTemp = översättEttOrd(svenska[i], engelska[i], försök)
            if resultatTemp == 1:
                break
            
        resultat += resultatTemp

    return resultat, len(svenska) - resultat

# Kör programmet
def main():    
    presentaion()

    rätt, fel = glosförhör()

    # Resultatet presenteras för användaren med antalet rätta samt felaktiga svar.
    print("\nDu hade {} rätt och {} fel".format(rätt, fel))


main()