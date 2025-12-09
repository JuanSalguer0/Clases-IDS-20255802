from os import system
if system("clear") != 0: system("cls")

#Ejercicio 1

"""
Descripción del Problema
Adrián realiza un prototipo de programa para determinar si una empresa tiene saldos positivos onegativos.

Él empieza formando las bases del código escribiendo un número y determinando si es positivo o negativo. Escribra un código querealice esta acción

Entrada
Recibirás un número entero 
.

Salida
Deberás mostrar "Positivo" en caso de que el número sea Positivo.

Deberás mostrar "Negativo" en caso de que el número sea Negativo.
"""
"""
N = int(input(""))

if N >= 0:
    print("Positivo")
else:
    print("Negativo")
"""

#Ejercicio 2

"""
Descripción
Leer un numero entero S y mostrar como salida el numero par posterior y el número impar anterior.

Entrada
Un número entero S.

Salida
El número par posterior y el número impar anterior al número entero leído.

Ejemplo
"""

"""
S = int(input(""))

print(S % 2)

if S % 2 == 0:
    pp = S + 2
    ia = S - 1
else:
    pp = S + 1
    ia = S - 2
    
print(pp)
print(ia)
"""

#Ejercicio 3
"""
c1 = float(input(""))
c2 = float(input(""))
c3 = float(input(""))
c4 = float(input(""))
c5 = float(input(""))
c6 = float(input(""))

promedio = (c1+c2+c3+c4+c5+c6)/6

if promedio > 9.5:
    print("Gana permio :)")
else:
    print("No gana premio :(")
"""

#Ejercicio 4
"""
N = int(input(""))

cnt7 = 0
cnt5 = 0

for i in range (N):
    numeros = int(input(""))
    if numeros ==7:
        cnt7 = cnt7 + 1
    elif numeros == 5:
        cnt5 = cnt5 + 1
        
print (cnt7)
print (cnt5)
"""

#Ejercicio 5
"""
N = int(input(""))
Pa, Pb, Pc = map(int, input().split())

for i in range (N):
    combo = input().strip()
    total = 0
    
    for boton in combo:
        if boton == "A":
            total = total + Pa
        if boton == "B":
            total = total + Pb
        if boton == "C":
            total = total + Pc
    print(total)
"""

#Ejercicio 6

"""
N = int(input(""))

for i in range(N):
    nombre = input("")
    if len(nombre) <= 6:
        print("No vale la pena")
    elif len(nombre) >= 8:
        print("Si aguanto otro desarrollo de personaje")
    else:
        print("Dios no creo aguantar esta vez")
"""

#Ejercicio 7
"""
x, y = map(int, input().split())

if x > y :
    print(x)
else:
    print(y)
"""

#Ejercicio 8
"""
N = int(input())
total = 0

for i in range (N):
    edades = int(input())
    if edades >= 15:
        total = total + 1 
print(total)
"""

#Ejercicio 9
"""
conectadoOdesconectado = input()
if conectadoOdesconectado.lower() == "conectado":
    print("Ola Ivan")
elif conectadoOdesconectado.lower() == "desconectado":
    print("Ol...")
"""

#Ejercicio 10 
"""
N = int(input(""))

for i in range(N):
    P = int(input(""))
    if P >= 3:
        print("Ok")
    else:
        print("No")
"""

