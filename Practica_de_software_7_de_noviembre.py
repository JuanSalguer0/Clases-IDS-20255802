from os import system
if system("clear") != 0: system("cls")

moderador = input("Ingrese el nombre del moderador: ")
contraseña = "ESEN"  
menu = True
moderarcliente = True
moderarproducto = True

codigounicocliente = []
nombrecliente = []
correocliente = []
telefonocliente = []

codigounicoproducto = []
nombreproducto = []
categoriaproducto = []
precioproducto = []

clientes = {}
productos = {}

contraseña_de_usuario = input("Favor ingrese la contraseña para moderar el menu: ")

while contraseña_de_usuario != contraseña:
    print("Contraseña incorrecta")
    contraseña_de_usuario = input("Favor ingrese la contraseña para moderar el menu: ")
else:
    print(f"Hola {moderador.capitalize()}, esperamos que este bien diganos que desea moderar hoy: ")
    while menu:
        opcion = int(input("Moderar clientes [1]\nModerar productos [2]\nsalir del menu [3]\n"))
        if opcion == 3:
            menu = False
        elif opcion == 1:
            moderarcliente = True
            while moderarcliente:
                print("¿Qué desea moderar del cliente?")
                opcioncliente = int(input("Registrar codigo de cliente [1]\nRegistrar nombre de cliente [2]\nRegristrar correo del cliente [3]\nRegistrar telefono del cliente [4]\nRegresar al menu [5]\n"))
                if opcioncliente == 5:
                   moderarcliente = False
                elif opcioncliente ==1:
                    codigocliente = input("Ingrese el codigo del cliente, recuerde que debera de poner 4 caracteres, el primer caracter debe de tener una 'C' y el resto de caracteres deben de ser numero en el resto de caracteres\n")
                    condicion1 = (len(codigocliente) == 4)
                    condicion2 = (codigocliente[0]=="C")
                    condicion3 = (codigocliente[1].isdigit(), codigocliente[2].isdigit(), codigocliente[3].isdigit() == True)
                    if condicion1 and condicion2 and condicion3 == False:
                        print("El codgio esta mal... vuelva a escribirlo")
                    else:
                        print(f"el codigo es {codigocliente}")
                        codigounicocliente.append(input("Digite el codigo unico del cliente para regristrarlo: "))