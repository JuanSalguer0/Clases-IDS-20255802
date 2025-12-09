from os import system
if system("clear") != 0: system("cls")

#Este modulo va a contener funciones "Modulo seria un archivo .py en el que deposito diferentes elementos así como funciones"
#Para crear la funciión, una función tiene 2 tiempos, una definición y una llamda
#Vamos a definir una función

def mi_funcion():
    """Esta funcion imprime un saludo"""
    print("Hola mundo")
    print("Amigo usuario")
    print("Gracias por usar nuestro sistema")
    
    
#Vamos a llamar la funcion, dentro de los parentesis deberia de haber argumentos si es que hay
#Vamos a recibir informacion desde afuera de la funcion

def capturar_nombre():
    """Esta funcion recibe valores por medio de input"""
    nombre_input = input("Escriba su nombre: \n::")
    apellido_input = input("Digite su apellido: \n::")
    nombre_completo = f"{nombre_input.capitalize()} {apellido_input.capitalize()}"
    print(nombre_completo)


def capturar_usuario(nombre, edad):
    """Esta funcion recibe valores por medio de argumentos"""
    nombre_usuario = nombre
    #ahora mi funcion me va a pedir que cuando la este llamando debo de poner dos valores, uno corresponde al nombre y el segundo a la edad
    edad_usuario = edad
    texto = f"El usuario {nombre_usuario.title()} tiene {edad_usuario} años de edad."
    print(texto)


#Llamando a las la funcion capturar nombre

"""
#Llamado a la funcion capturar usuario
capturar_usuario(input("Ingrese su nombre: "), int(input("Ingrese su edad: ")))
"""

#funcion que devuelve un valor
def calculo_de_impuesto(ventas):
    """Esta funcion calcula el valor del impuesto"""
    if ventas < 500:
        tasa_impuesto = 0.1
    else:
        tasa_impuesto = 0.25
    return tasa_impuesto

#return sirve para hacer explicito que no necesito, no le estoy pidiendo que me imprima un valor, le estoy pidiendo que me devuelva un valor especifico

ventas = 100
#se puede llamar ala funcion entre variables fuera de la funcion
"""
tasa_calculada = calculo_impuesto(ventas)
monto_impuesto = calculo_impuestp(ventas)*ventas
"""


print(f"El valor de la ventafue de ${ventas:,.2f}, \nla tasa de impuesto es {calculo_de_impuesto(ventas):,.2f} \ny el monto por tanto es ${calculo_de_impuesto(ventas)*ventas:,.2f}")

#cuando estoy definiendo una funcion lo que va adentro de los parentesis se llaman parametros y cuando estoy llamando dicha funcion lo que va adentro de los parentesis se llama argumentos
#Cuando llamo a la funcion y le estoy suamndo valores a los parametros estos se llaman arguemntos