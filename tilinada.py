from os import system
if system("clear") != 0: system("cls")


agente = 'encargado' # Variable con valor de encargado
aplicación = True
platillo = [] # Variable del lista de platillos
precios = [] # Variable de lista de precios

nombre_agente = input('Favor ingrese el nombre del agente: ') # Input para que el usuario ingrese el nombre del agente

while nombre_agente.lower() != agente: # While para indicar que hasta que no se ponga el valor del agente correcto lo siga escribiendo.
    print('Agente no registrado')
    nombre_agente = input('Favor ingrese el nombre del agente: ')
else:
    print(f"Hola {agente.lower()}, esperamos que este bien\ndiganos que desea realizar hoy:")
    while aplicación:
        opciones = int(input('1. Creación de platillos 2. Consulta de platillos y precios 3. Colocar un pedido 4. Salir')) # La variable opciones que permitirpa al usuario decidir que opción quiere
        if opciones == 1:
            platillo.append(input('Ingrese el nombre del platillo a crear: ').lower())
            precios.append(float(input('Ingrese el precio del platillo a crear: ')))
        elif opciones == 2:
            if len(platillo) == 0:
                print('Actualmente no hay platillos ingresados')
            else:
                for a in range(len(platillo)):
                    print(f'{platillo[a]}: ${precios[a]}')
        elif opciones == 3:
            platillo_a_elegir = input('Indique el nombre del platillo para su orden: ')
            if platillo_a_elegir.lower() in platillo:
                orden_platillo = platillo.index(platillo_a_elegir.lower())
                print(f'Usted ha elegido {platillo[orden_platillo]} con un precio de {precios[orden_platillo]}')
            else:
                print('El platillo ingresado no existe')
        elif opciones == 4:
            aplicación = False