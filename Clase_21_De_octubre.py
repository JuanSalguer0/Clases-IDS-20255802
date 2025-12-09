from os import system
if system("clear") != 0: system("cls")

"""
lista = [1, 2, "tres",["ene", "feb", "mar"]]
print(len(lista))
print(lista)
print(lista[3][2][1])
"""

numeros = [1, 2, 3]
meses = ["ene", "feb", "mar"]
print(len(numeros), len(meses))
print(numeros + meses)
print("Hola")
