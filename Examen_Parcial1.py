from os import system
if system("clear") != 0: system("cls")

#Ejercicio 1
"""
X1 = int(input(""))
X2 = int(input(""))

condicion1 = (X1==X2)
print(condicion1)
"""
#Ejercicio2
#Lee dos números enteros y muestra True si el primero es múltiplo del segundo. False en caso contrario.
"""
N1 = int(input(""))
N2 = int(input(""))

Condicion1 = (N1 % N2 == 0)

print(Condicion1)
"""

#Ejercicio 3
#Devuelve True si la palabra termina con esa letra (sin importar mayúsculas o minúsculas).
"""
Cadena1 = input("")
Cadena2 = input("")

condicion1 = (Cadena1.lower()[-1] == Cadena2.lower())

print(condicion1)
"""

#Ejercicio 4
#Lee una palabra y muestra True si se lee igual al derecho y al revés, independientemente de mayúsculas o minúsculas
"""
palabra = input("")
condicion1 = (palabra.lower() == palabra.lower()[::-1])
print(condicion1)
"""

#Ejercicio 5
#Lee una palabra y una letra, e imprime True si la palabra contiene esa letra, sin importar el caso.
"""
palabra1 = input("")
letra = input("")

condicion1 = (palabra1.lower().count(letra.lower()) >= 1) 

print(condicion1)
"""

#Ejercicio 6
#Recibe un valor (sin comillas) y muestra True si es de tipo entero, False en caso contrario.
#Entrada(input) = -45
#Salida(print) = True

V1 = (input())
contarpunto = V1.count(".") == 0
print(contarpunto)



#ejercicio 7
#Recibe un supuesto número de DUI, el cual debe validar que se cumplan las siguientes condiciones:
#El largo debe de ser exactamente de 10 caracteres
#El noveno carácter debe ser “-“
#Validar únicamente que el último carácter es número entero.

d_u_i = input("")
condicion1 = (len(d_u_i) == 10)
condicion2 = (d_u_i[8]=="-")
condicion3 = (d_u_i[-1].isdigit()==True)
print(condicion1 and condicion2 and condicion3)


