# 2022-09-09
# Viktor Lindén, Erik Stare

# Funktion som frågar efter ett heltal mellan 1 och 10.
def beOmHeltal():
    # Skapar en loop som fortsätter till rätt inmatning har givits.
    while True:
        heltal = input("Skriv ett heltal mellan 1-10:")

        # Om det inmatade talet är inom det korrekta spannet ska talet returneras.
        if heltal <= 10 and heltal >= 1:
            return heltal

        # Annars be användaren göra ett nytt försök.
        else:
            print("Försök igen, talet ska ligga inom spannet 1-10")

x = beOmHeltal()