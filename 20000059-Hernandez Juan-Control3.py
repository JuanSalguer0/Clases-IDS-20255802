from os import system
if system("clear") != 0: system("cls")

encargado = "Encargado"  #Aqui podemos ver la creación de cada variable la cual usaremos mas adleante para trabajar de manera ordenada
menu = True #Esta nos servira para poder trabajar mediante un while cuando el usuario siga activo en el menu
platillo = [] #Estas variables sonp para la creación de listas de platillos y precios
precios = []

agente = input("Favor ingrese el nombre del agente: ")

while agente.capitalize() != encargado:   #aquí se le pide la autentificación al agente para ver si es un encargado para poder continuar con el resto del progorama
    print("Agente no registrado")
    agente = input("Favor ingrese el nombre del agente: ")
else:
    print(f"Hola {encargado.lower()}, esperamos que este bien\ndiganos que desea realizar hoy:")
    while menu:
        opcion = int(input("1.Agregar platillos, 2.Consultar platillos y precios, 3.Colocar un pedido, 4.salir: "))  #Aqui se observa el menu y las opciones que se tiene para poder realizar durante el menu
        if opcion == 4: #esta regla es para salir del menu
            menu = False
        elif opcion == 1:   #Aqui pedimos al encargado poder agregar algun plato al menu
            platillo.append(input("Digite el nombre del platillo: ").lower())
            print(platillo)
            precios.append(input("Digite el nombre del precio: "))
            print(precios)
        elif opcion == 2:   #Aqui puede pedir los platos y precios que se dieron anteriormente
            if len(platillo) == 0:
                print ("Actualmente no hay platillos ingresados")
            else:
                for a in range(len(platillo)):
                    print(f"{platillo[a]}: ${precios[a]}")
        elif opcion == 3:   #Aqui el usuario puede pedir que plato quiere y a que precio se le dara 
            pu = input("Ingrese el nombre de su platillo: ")
            if pu.lower() in platillo:
                indice = platillo.index(pu.lower())
                print(f"Usted a elejido el platillo {platillo[indice]} con un precio de {precios[indice]}")
            else:
                print("El platillo no existe")
        