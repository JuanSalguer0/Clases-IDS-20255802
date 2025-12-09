from os import system
if system("clear") != 0: system("cls")

palabra1 = input("")
letra = input("")

condicion1 = (palabra1.lower().count(letra.lower()) >= 1) 

print(condicion1)