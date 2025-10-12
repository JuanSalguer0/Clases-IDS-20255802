"""
Enero = float(input("Ingrese la cantidad de enero: "))
Febrero = float(input("Ingrese la cantidad de febrero: "))
Marzo = float(input("Ingrese la cantidad de marzo: "))

print(f"Tu cantidad es de {round((Enero*1.25) + (Febrero*1.38) + (Marzo*1.14),2)}")
"""

#Crear una lista con los dias laborales de la seamana, le pediremos los valores de las cantidades vendidas, imprima la nueva lista
"""
DIAS = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
Lunes = int(input("Cuanto vendiste el Lunes: "))
DIAS[0] = Lunes
Martes = int(input("Cuanto vendiste el Martes: "))
DIAS[1] = Martes
Miercoles = int(input("Cuanto vendiste el Miercoles: "))
DIAS[2] = Miercoles
Jueves = int(input("Cuanto vendiste el Jueves: "))
DIAS[3] = Jueves
Viernes = int(input("Cuanto vendiste el Viernes: "))
DIAS[4] = Viernes
print(DIAS)
"""

#Crear una consulta de 6 peticiones para que cada niño mencione su fruta favorita, luego imprimir la lista actualizada 

"""
Fruta = ["Niño Uno","Niño Dos","Niño tres"]
print(Fruta)

ninio = int(input())
fruta = input()
Fruta[ninio] = fruta
print(Fruta)
ninio = int(input())
fruta = input()
Fruta[ninio] = fruta
print(Fruta)
ninio = int(input())
fruta = input()
Fruta[ninio] = fruta
print(Fruta)
"""
#Crearemos una conexion de los nombres de 7 alumnos que entraron en el aula

"""
alumnos = ["Juan", "Ana", "Pedro"]

orden = int(input("Orden en el que entraste(1-3): "))
print(f"El niño que entro en orden {orden} se llama {alumnos[orden-1]}")
"""
#Vamos a capturar nombres y apeidos, apa rtir de ello hay que trabajar para la empresa INSD, se le pide que construya dos propuestas de correo a partir de estos datos ingresados. Si la persona incluyendo errores escribe mas de una mayuscula, ha yque mostrarlo todo como minuscula.

"""
nombre = input("Nombre: ")
apellido = input("Apellido: ")

print(f"{nombre.lower()}.{apellido.lower()}@ISND.com")
print(f"{nombre.lower()[0]}.{apellido.lower()}@ISND.com")
"""

#el usuario tien que ingresar un salario, ahora el salario se ingresa de forma diferente pues este lelvare simbolos

"""
salario = input("Ingrese su salario: ")

print(salario[0]=="$")
print(salario.count("$")==1)
"""

#A usted se le asignado una palabra inccriptada la cual sera su contrase;a... para poder decifrarla bla bla bla 

palabra = "dfiaunasdiwasd"
print(palabra[::3])