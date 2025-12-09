from os import system
if system("clear") != 0: system("cls")

numeros = [1, 2, 3, 4]
#print(len(numeros))
#Bucle finito (for), coleccion str, lista, tupla, dict
#Bucle infinto 

"""
for x in numeros:
    print("Hola")
"""

"""
palabra = "Aulas"
print(len(palabra))

for x in palabra:
    print("Hola")
"""


#dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

"""
for x in dias:
    print(x[:2])
"""

"""
for i in range(0,10,2):
    print(i)
"""

"""
personas = ["Ana", "Luis", "Luisa"]
for p in personas:
    for l in p:
        print(l)
"""

"""
valores = [[1,3,6], 
           [2,7,4], 
           [6,5,9], 
           [1,10,20]]

mayores = []
minimo = int(input("Ingrese el valor minimo:\n"))

for x in valores:
    for y in x:
        if y > minimo:
            mayores.append(y)
            
print(mayores)
"""

"""
inicio = 0
maximo = 5

while inicio < maximo:
    print("Saludo")
    inicio = inicio + 1
"""

"""
presupuesto = 1000
gasto = 0

while gasto <= presupuesto:
    compra = float(input("Digite el valor de compra: "))
    gasto += compra
gasto -= compra

print(gasto)
"""

estado = "Conectado"

while estado.lower() == "conectado":
    print("Hola sebas")
    estado = input("Digite su estado: ")
