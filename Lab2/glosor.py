#2022-08-31
#Viktor Lindén, Erik Stare

from unittest import result


svenska = ["Bord", "Dator", "Bil", "Blomma", "Flagga", "Svår"]
engelska = ["Table", "Computer", "Car", "Flower", "Flag", "Hard"]

# Presenterar programmet för användaren. Skriver ut vad som förväntas av användaren. \n används för att göra programmet mer estetiskt snyggt.
print("Detta är ett glosförhör. Skriv rätt översättning till engelska utifrån det svenska ord som presenteras.\n")

resultat = 0
for i in range(len(svenska)):
    if i==5:
        tries = 0
        while True:
            if input(svenska[i] + ": ").lower() == engelska[i].lower():
                print("Bra!\n")
                resultat += 1
                break
            else:
                tries += 1
            
            if tries == 3:
                print("Ajdå, rätt svar var " + engelska[i].lower())
                print()
                break
            else:
                print("Ajdå, försök igen!")

    else:    
        if input(svenska[i] + ": ").lower() == engelska[i].lower():
            print("Bra!\n")
            resultat += 1
        
        else:
            print("Ajdå, rätt svar var " + engelska[i].lower())
            print()

print("\nDu hade {} rätt och {} fel".format(resultat, len(svenska)-resultat))