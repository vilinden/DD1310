#2022-09-12
#Viktor Lindén, Erik Stare

# Lägger varje rad i given fil till varsitt element i lista
def raderTillLista(filepath):
    try:
        fil = open(filepath, "r")
        lista = fil.readlines()
        for i in range(len(lista)):
            lista[i] = lista[i].replace("\n", "")
        fil.close()
        return lista
    except:
        return []

# Kör programmet
def main():
    print(raderTillLista("Idas.txt"))
    print()
    print(raderTillLista("randomFil"))

main()