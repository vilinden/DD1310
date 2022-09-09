# 2022-09-09
# Viktor Lindén, Erik Stare

# Skriver ut en uppmuntrande fras
def uppmuntrandeFras():
    print("Vad fin du är idag!")

# Skriver ut ett skämt
def skämt():
    print("Den ena säger till den andra: \"Jag fryser\".\Den andra svarar: \"Men gå bort till hörnet, där är det 90 grader.\"")

# Frågar användaren om hen vill höra en uppmanande fras eller ett skämt och användaren ska då svara 1 eller 2 för respektive.
if input("Vill du höra en uppmuntrande fras (1) eller ett skämt (2)?") == 1:
    uppmuntrandeFras()
else:
    skämt()