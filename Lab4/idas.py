#2022-09-12
#Viktor Lindén, Erik Stare

fil = open("Idas.txt", "r")
text = fil.readlines()
print("readlines\n", text)
fil.close()

print()

fil = open("Idas.txt", "r")
text = ""
for line in range(4):
    text += fil.readline()
print("readline\n", text)
fil.close()

print()

fil = open("Idas.txt", "r")
text = fil.read()
print("read\n", text)
fil.close()