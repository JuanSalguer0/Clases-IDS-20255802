from os import system
if system("clear") != 0: system("cls")


"""
aprobacion = True

while aprobacion:
    eleccion = input("Quieres seguir jugando (Y/N):")
    if eleccion[0].lower() == "n":
        aprobacion = False
    elif eleccion[0].lower() == "y":
        print("Me alegra que quieras seguir jugando")
"""

#alumnos = []

"""
alumno = input("Digite el nombre> \n")
alumnos.append(alumno)
alumno = input("Digite el nombre> \n")
alumnos.append(alumno)
alumno = input("Digite el nombre> \n")
alumnos.append(alumno)
print(alumnos)
"""

"""
for a in range(int(input("Digite la cantidad de alumnos a registrar: "))):
    alumno = input("Digite el nombre: ")
    alumnos.append(alumno)
    
print (alumnos)
"""

menu_iniciado = True
alumnos = []

while menu_iniciado:
    opcion = int(input("1.Agregar, 2.Consultar, 3.Modificar, 4.Borrar, 5.Salir: "))
    if opcion == 5:
        menu_iniciado = False
    elif opcion ==1:
        alumnos.append(input("Digite el nombre del alumno: "))
        print(alumnos)
    elif opcion == 2:
        for a in alumnos:
            print(a)
    elif opcion == 3:
        indice = int(input("Digite el numero del alumno (1-3): "))
        nuevo = input("Digite el nombre nuevo: ")
        alumnos[indice-1] = nuevo
    elif opcion == 4:
        indice = int(input("Digite el numero del alumno del 1 al 3 a popear: "))
        alumno_borrado = alumnos.pop(indice-1)
        print(f"Hemos borrado a: {alumno_borrado}")
    else:
        print("Esta opcion no es valido")



print("Gracias por usar nuestro sistema ")