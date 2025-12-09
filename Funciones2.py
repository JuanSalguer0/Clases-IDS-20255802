from os import system
if system("clear") != 0: system("cls")

#otro modulo para comprneder las funciones

#definimos la funcion
def describri_mascota(tipo_animal:str, nombre_mascota: str ):
    """Esta funcion describe una mascota"""
    print(f"Mi mascota se llama {nombre_mascota.capitalize()}")
    print(f"Y es un tipo de animal {tipo_animal.lower()}.")
    
#llamamos la funcion
describri_mascota("Perro", "phoenix")
describri_mascota("Gato", "misifus")