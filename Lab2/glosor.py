#2022-08-31
#Viktor Lindén, Erik Stare

# Etablerar listor för glosorna. Ord med samma index är översättningar på varandra.
svenska = ["Bord", "Dator", "Bil", "Blomma", "Flagga", "Svår"]
engelska = ["Table", "Computer", "Car", "Flower", "Flag", "Hard"]

# Presenterar programmet för användaren. Skriver ut vad som förväntas av användaren. \n används för att göra programmet mer estetiskt snyggt.
print("Detta är ett glosförhör. Skriv rätt översättning till engelska utifrån det svenska ord som presenteras.\n")

# Etablerar variabel för att hålla koll på antalet rätta översättningar.
resultat = 0

# Loopar igenom varje index för den svenska listan
for i in range(len(svenska)):
    # Om indexet är 5, så är det den svåra glosan som förhörs och användaren ska därför få flera försök. Därför initierar vi en while-loop
    if i==5:
        # Loopar igenom max 3 gånger för att ge användaren flera chanser att svara rätt.
        for tries in range(3):
            # Om användaren skriver rätt översättning beröms användaren, ett poäng ges till resultatet samt att vi break:ar for-loopen för att gå vidare i programmet.
            if input(svenska[i] + ": ").lower() == engelska[i].lower():
                print("Bra!\n")
                resultat += 1
                break
            
            # Om användaren är på sitt 3e och sista försök så ska det korrekta svaret presenteras.
            if tries == 2:
                print("Ajdå, rätt svar var " + engelska[i].lower())
                print()
            # Om användaren svarade fel på ett av de 2 första försöken så ska användaren ges ett nytt försök till att gissa rätt. Programmet ber användaren försöka igen.
            else:
                print("Ajdå, försök igen!")

    # Om det inte är den svåra glosan som efterfrågas så körs följande sats.
    else: 
        # Om inmatningen är korrekt beröms användaren och ett poäng ges till resultatet.   
        if input(svenska[i] + ": ").lower() == engelska[i].lower():
            print("Bra!\n")
            resultat += 1
        # Om fel svar angets ska användaren presenteras av det rätta svaret.
        else:
            print("Ajdå, rätt svar var " + engelska[i].lower())
            # Den tomma print-funktionen används endast för att göra programmet mer estetiskt tilltalande.
            print()

# Resultatet presenteras för användaren med antalet rätta samt felaktiga svar.
print("\nDu hade {} rätt och {} fel".format(resultat, len(svenska)-resultat))