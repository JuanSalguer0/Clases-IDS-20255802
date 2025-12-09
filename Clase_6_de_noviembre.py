from os import system
if system("clear") != 0: system("cls")

usuarios = ["Juan", "Luis", "Diana", "Pao", "Jaime"]
edades = [20, 19, 21, 22, 18]
frutas = ["mango", "fresa", "pera", "sandia", "piña"]

"""
for i, usuarios in enumerate(usuarios,start=1):
    print(f"{i} {usuarios}")
"""

for usuarios, edades, frutas in zip(usuarios, edades, frutas):
    print(f"{usuarios} tiene {edades} años y le gusta el/la {frutas}")