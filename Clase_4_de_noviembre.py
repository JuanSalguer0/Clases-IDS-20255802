from os import system
if system("clear") != 0: system("cls")

#vamos a crear nuesto primer set (Docstring, un string de documentacion)
"""
my_set = {"rojo", "verde", "negro", "azul", "rojo", "azul",}
print(type(my_set))
print(len(my_set))
print(my_set)
"""

#colores = {"rojo", "verde", "negro", "azul", "rojo", "azul",}

"""
mi_masctoa = { "tipo": "perro", 
              "nombre": "milo", 
              "edad": 4, 
              "personalidad": "Lobo solitario"}

print(type(mi_masctoa))
print(len(mi_masctoa))
print(mi_masctoa)
"""

birthdays = {
    "Alice": "Apr 1",
    "Bob": "Dec 12",
    "Carol": "Mar 4"
}
print(type(birthdays))
birthdays["Carol"] = "Sep 12"
print(birthdays["Carol"])
birthdays["Pau"] = "Jul 31"
print(birthdays)
del birthdays["Bob"]
print(birthdays)

for person, date in birthdays.items():
    print(f"El cumpleaños de {person} es en {date}")