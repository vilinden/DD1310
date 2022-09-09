# Rovarspråk av Viktor Lindén, Erik Stare
# Skrivet den 2022-09-05
konsonanter="bcdfghjklmnpqrstvwxz" 
print("Hej välkommen till rövarspråksöversättaren") 
svenska=input("Vilken bokstav vill du översätta:") 
rövarspråk="" 
# 1 svenska kommer ursprungligen att vara en bokstav, lagra svenska i 
# variabeln bokstav 
for i in svenska:
    bokstav = i
    # 3 skriv en for-slinga plockar en bokstav i taget ur ordet svenska för 
    # översättning med hjälp av if-satsen. Extra klurighet, behöver något mer 
    # än if-satsen i slingan?(Kan bero lite på hur ni löst if-satsen) 
    # 2 Skriv en if-sats som kontrollerar om bokstaven är en konsonant och i så fall 
    # översätter den till rövarspråk 
    if bokstav.lower() in konsonanter:
        bokstav += "o" + bokstav
    rövarspråk += bokstav 
print("Översättningen blir: " + rövarspråk) 