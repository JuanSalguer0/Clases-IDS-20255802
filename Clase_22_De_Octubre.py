from os import system
if system("clear") != 0: system("cls")

"""
numeros = ["uno", "dos", "tres", "cuatro"]
print(numeros[0])
print(numeros[1])
print(numeros[2])
print(numeros[3])

print(numeros.count("dos"))

nombres = ["Ana", "Antonio", "Ana", "Jose"]
r_a = 0
r_a = r_a + nombres[0].lower().count("a")
r_a = r_a + nombres[1].lower().count("a")
r_a = r_a + nombres[2].lower().count("a")
r_a = r_a + nombres[3].lower().count("a")
print(nombres[0].lower().count("a"))
print(r_a)
"""
"""
nombre = ["Ana", "Antonio", "Paulina", "Jose"]
print(nombre)
nombre[2] = "Pablo"
print(nombre)
#nombre.append("Hazel")
#nombre.append(input("Ingrese el nuevo nombre:\n"))
nombre.insert(3, "Sebas")
#nombre.insert(3, input("Ingrese el nuevo nombre:\n"))
print(nombre)
#nombre.remove("Sebas")
nombre_borrado = nombre.pop(int(input("Indice a borrar:"))-1)
print(nombre)
print(nombre_borrado)
"""

"""
nota = float(input("Indique la nota del estudiante aquí: \n :::"))

if nota>=6:
    print("paso")
else:
    print("No aprobo")
"""
"""
nota = float(input("Indique la nota del estudiante aquí: \n :::"))

if nota >= 10:
    print("E")
else:
    if nota > 7:
        print("MB")
    else:
        if nota > 5:
            print("B")
        else:
            if nota > 3:
                print("M")
            else:
                if nota >= 0:
                    print("Pucta maje, cambaite de carrera")
"""

"""
monto = float(input("Digite el monto: \n"))
tipo = input("Ingrese el tipo (Local/Exportacion): \n")
impuesto = 0

if tipo.lower() == "local":
    if monto > 500:
        impuesto = 0.1
    else:
        if monto > 200:
            impuesto = 0.08
        else:
            if monto > 50:
                impuesto = 0.06
            else:
                if monto <= 50:
                    impuesto = 0.00
elif tipo.lower() == "exportacion":
    if monto > 500:
        impuesto = 0.14
    else:
        if monto > 200:
            impuesto = 0.12
        else:
            if monto > 50:
                impuesto = 0.1
            else:
                if monto <= 50:
                    impuesto = 0.00
else:
    print("invalido tilin")


print(f"El impuesto a pagar de tipo {tipo.lower()} por venta de {monto:,.2f}")
print(f"es de {monto*impuesto:,.2f}")
print(f"La suma total a pagar es de {monto + monto*impuesto:,.2f}")
"""

"""
monto = float(input("Digite el monto: \n"))
tipo = input("Ingrese el tipo (Local/Exportacion): \n")
impuesto = 0

if tipo.lower() == "local":
    if monto > 500:
        print(f"El monto a pagar es {monto + monto*0.10:,.2f}")
    else:
        if monto > 200:
            impuesto = 0.08
        else:
            if monto > 50:
                impuesto = 0.06
            else:
                if monto <= 50:
                    impuesto = 0.00
elif tipo.lower() == "exportacion":
    if monto > 500:
        impuesto = 0.14
    else:
        if monto > 200:
            impuesto = 0.12
        else:
            if monto > 50:
                impuesto = 0.1
            else:
                if monto <= 50:
                    impuesto = 0.00
else:
    print("invalido tilin")

print(f"El impuesto a pagar de tipo {tipo.lower()} por venta de {monto:,.2f}")
print(f"es de {monto*impuesto:,.2f}")
"""

#nombre = ["Ana", "Sebas", "Maria", "Carla"]
#nombre = [1, 2, 3]
#nombre_buscar = input("Nombre a buscar: \n")
"""
for n in nombre:
    if n == nombre_buscar.capitalize():
        print("Ya lo encontre")
    else:
        print("Aqui no esta")
"""
#print(len(nombre[0]))









nota1 = float (input(""))
nota2 = float (input(""))
nota3 = float (input(""))

puntaje1 = float(input())
puntaje2 = float(input())
puntaje3 = float(input())

promedio = (int(nota1*puntaje1))+(int(nota2*puntaje2))+(int(nota3*puntaje3))
print(promedio)













