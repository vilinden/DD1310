# 2022-09-09
# Viktor Lindén, Erik Stare

# Presenterar programmet för användaren. Skriver ut vad som förväntas av användaren. \n används för att göra programmet mer estetiskt snyggt.
def presentaion():
    print("Detta är ett glosförhör. Skriv rätt översättning till engelska utifrån det svenska ord som presenteras.\n")

def översättEttOrd(svenska, engelska, försök = 0):
    inmatning = input("Vad är {} på engelska? ".format(svenska))
    if inmatning.lower() == engelska.lower():
        print("Bravo!")
        return 1
    elif försök == 0:
        print("Det var tyävrr fel! Rätt svar är "+ engelska)
    else:
        print("Det var tyvärr fel, försök igen!")
    return 0


# Etablerar listor för glosorna. Ord med samma index är översättningar på varandra.
svenska = ["Bord", "Dator", "Bil", "Blomma", "Flagga", "Svår"]
engelska = ["Table", "Computer", "Car", "Flower", "Flag", "Hard"]

# Etablerar variabel för att hålla koll på antalet rätta översättningar.
resultat = 0

presentaion()

# Loopar igenom varje index för den svenska listan
for i in range(len(svenska)):
    if i != len(svenska) - 1:
        resultat += översättEttOrd(svenska[i], engelska[i])
    else:
        resultatTemp = 0
        for försök in range(3, 0, -1):
            resultatTemp = översättEttOrd(svenska[i], engelska[i], försök)
            if resultatTemp == 1:
                break
        
        resultat += resultatTemp

# Resultatet presenteras för användaren med antalet rätta samt felaktiga svar.
print("\nDu hade {} rätt och {} fel".format(resultat, len(svenska)-resultat))