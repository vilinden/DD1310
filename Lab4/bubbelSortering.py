#2022-09-12
#Viktor Lindén, Erik Stare

# Sorterar given lista enligt bubbleSort algoritmen.
def bubbleSort(lista):
    changed = True
    while changed:
        changed = False
        for i in range(len(lista)-1):
            if lista[i+1] < lista[i]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
                changed = True

    return lista

# Kör programmet
def main():
    list = [1, 5, 3, 6, 10, 2, 5, 10]
    print(bubbleSort(list))

main()