#2022-09-21
#Viktor Lindén, Erik Stare

from operator import contains

# Räknar antalet ord och meningar i en given sträng
def räknaOrdOchMeningar(text):
    # Meningar slutar på punkt och kan därför tas fram med hjälp av att split:a på punkter
    meningar = text.split(".")

    # Genom att split:a på punkter kommer ett tomt element med i listan som bör tas bort då detta inte är en mening.
    if "" in meningar:
        meningar.remove("")

    # Split:ar strängen på mellanrum för att få ut orden.
    ord = text.split()

    # Printar ut längden på listorna för att se antalet ord och meningar.
    print(str(len(ord)) + " ord och " + str(len(meningar)) + " meningar")

# Kör programmet
def main():
    sträng = "Hej det här är en mening. Här \tär en annan mening. Och det här är den tredje."
    räknaOrdOchMeningar(sträng)

main()