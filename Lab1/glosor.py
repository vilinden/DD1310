#2022-08-31
#Viktor Lindén, Erik Stare

# Presenterar programmet för användaren. Skriver ut vad som förväntas av användaren. \n används för att göra programmet mer estetiskt snyggt.
print("Detta är ett glosförhör. Skriv rätt översättning till engelska utifrån det svenska ord som presenteras.\n")

# Sparar inmatningsvärdet i variabeln och gör om allt till gemener för att göra programmet mer användarvänligt.
svarBord = input("Bord: ").lower()
# Om det inmatade värdet matchar den rätta översättningen.
if svarBord == "table":
    # Om översättningen är korrekt beröms användaren.
    print("Bra!\n")
    # Om översättningen inte stämmer överrens beklagas det till användaren och det korrekta svaret presenteras.
else: print("Det var synd! Rätt svar är table.\n")

# Samma som tidigare repeteras med två nya glosor.
svarStol = input("Stol: ").lower()
if svarStol == "chair":
    print("Bra!\n")
else: print("Det var synd! Rätt svar är chair.\n")

svarProgrammering = input("Programmering: ").lower()
if svarProgrammering == "programming":
    print("Bra!\n")
else: print("Det var synd! Rätt svar är programming.\n")