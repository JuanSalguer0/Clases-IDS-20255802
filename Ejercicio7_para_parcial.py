"""
Enunciado

Un dragón duerme sobre una cadena de letras. Para que no despierte, debes contar cuántas veces aparece la letra z en la cadena.

Entrada:

Una cadena de hasta 100 caracteres en minúsculas.
Salida:

Un número entero con la cantidad de letras z.
Ejemplos:

Input	Output	Description
abrazozorrozorro
3
En la cadena abrazozorrozorro aparecen 3 letras z.

camino
0
En la cadena camino no aparece ninguna z.    
"""

def contar_zetas(cadena):
    return cadena.count('z')

cadena = input().strip()
print(contar_zetas(cadena))
