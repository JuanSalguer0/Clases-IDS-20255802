from os import system
if system("clear") != 0: system("cls")

palabra = input("")
condicion1 = (palabra.lower() == palabra.lower()[::-1])
print(condicion1)