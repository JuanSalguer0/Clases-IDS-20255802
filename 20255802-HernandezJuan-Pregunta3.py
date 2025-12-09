from os import system
if system("clear") != 0: system("cls")

Cadena1 = input("")
Cadena2 = input("")

condicion1 = (Cadena1.lower()[-1] == Cadena2.lower())

print(condicion1)