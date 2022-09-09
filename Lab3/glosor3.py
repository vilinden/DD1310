# 2022-09-09
# Viktor Lindén, Erik Stare

# Presenterar programmet för användaren. Skriver ut vad som förväntas av användaren. \n används för att göra programmet mer estetiskt snyggt.
def presentaion():
    print("Detta är ett glosförhör. Skriv rätt översättning till engelska utifrån det svenska ord som presenteras.\n")

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

def glosförhör(svenska, engelska, svårighet):
    # Etablerar variabel för att hålla koll på antalet rätta översättningar.
    resultat = 0

    # Loopar igenom varje index för den svenska listan
    for i in range(len(svenska)):
        resultatTemp = 0
        for försök in range(svårighet[i], 0, -1):
            resultatTemp = översättEttOrd(svenska[i], engelska[i], försök)
            if resultatTemp == 1:
                break
            
        resultat += resultatTemp

    return resultat


# Etablerar listor för glosorna. Ord med samma index är översättningar på varandra.
svenska = ["Bord", "Dator", "Bil", "Blomma", "Flagga", "Svår"]
engelska = ["Table", "Computer", "Car", "Flower", "Flag", "Hard"]
svårighet = [1, 1, 1, 1, 1, 3]

presentaion()

resultat = glosförhör(svenska, engelska, svårighet)

# Resultatet presenteras för användaren med antalet rätta samt felaktiga svar.
print("\nDu hade {} rätt och {} fel".format(resultat, len(svenska)-resultat))