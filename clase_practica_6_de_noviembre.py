from os import system
if system("clear") != 0: system("cls")

#Para usuarios

menu = True

while menu == True:
    codigo_unico_de_usuarios = []
    codigo_unico_de_usuarios = input("Ingrese su codigo de usuario: ")
    print(codigo_unico_de_usuarios)
    if codigo_unico_de_usuarios ==1:
        nombre_de_usuarios = []
        nombre_de_usuarios = input("Ingrese su nombre de usuario: ")
        if nombre_de_usuarios == 1:
            correo_de_usuarios = []
            correo_de_usuarios = input("Ingrese su correo de usuario: ")
            if correo_de_usuarios == 1:
                telefono_de_usuarios = []
                telefono_de_usuarios = input("Ingrese su telefono de usuario: ")
    menu = False

"""
usuarios = {"codigo unico": codigo_unico_de_usuarios,
            "nombre": nombre_de_usuarios,
            "correo": correo_de_usuarios,
            "telefono": telefono_de_usuarios,
                }
"""
"""
print(usuarios)
"""

"""
codigo_unico_de_productos = []
codigo_unico_de_productos = input("Ingrese el codgio de producto: ")
nombre_de_productos = []
nombre_de_productos = input("Ingrese el nombre del producto: ")
categoria_de_productos = []
categoria_de_productos = input("Ingrese la categoria del producto: ")
precio_de_productos = []
precio_de_productos = input("Ingrese el precio del producto: ")
"""

"""
productos = {"codigo unico": codigo_unico_de_productos,
            "nombre": nombre_de_productos,
            "categoria": categoria_de_productos,
            "precio": precio_de_productos,
                }

print(productos)
"""