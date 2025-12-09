"""
Después del desastre con el generador automático de correos y el intento de realizar un programa para encontrar los correos inválidos, la ESEN se dio cuenta de que el programa era demasiado simple y permitió que muchos correos incorrectos pasaran las pruebas.

Por esta razón, la ESEN quiere desarrollar un nuevo programa, más complejo y sofisticado, que les ayude a validar de mejor forma los correos y así tenerlos listos para sus alumnos de nuevo ingreso 2026.

Te han asignado la misión de crear este nuevo programa. Tu programa debe recibir un correo a validar e imprimir un mensaje que indique si es válido o inválido (True/False). Para que un correo se considere válido, debe cumplir las siguientes condiciones:

El correo contiene exactamente un @
Antes y después del @ debe haber al menos 3 caracteres
El correo debe contener al menos un punto
El correo no puede contener espacios
El correo no puede iniciar ni terminar con un punto
Restricciones
Todos los correos tendrán mínimo un arroba, aunque pueden tener varios.

Entrada
Una sola línea con un correo electrónico a validar.

Salida
Una sola línea con un mensaje que indique si el correo cumple todas las condiciones (True) o no (False).
"""

"""
def es_correo_valido(correo):
    # Verificar que el correo contenga exactamente un '@'
    if correo.count('@') != 1:
        return False
    
    # Dividir el correo en dos partes: antes y después del '@'
    parte_local, parte_dominio = correo.split('@')
    
    # Verificar que ambas partes tengan al menos 3 caracteres
    if len(parte_local) < 3 or len(parte_dominio) < 3:
        return False
    
    # Verificar que el correo contenga al menos un punto
    if '.' not in correo:
        return False
    
    # Verificar que el correo no contenga espacios
    if ' ' in correo:
        return False
    
    # Verificar que el correo no inicie ni termine con un punto
    if correo.startswith('.') or correo.endswith('.'):
        return False
    
    return True 
# Leer el correo desde la entrada estándar
correo = input().strip()
print(es_correo_valido(correo))
# Función para validar el 
"""

def es_correo_valido(correo):
    if correo.count('@') != 1:
        return False

    parte_local, parte_dominio = correo.split('@')
    
    if len(parte_local) < 3 or len(parte_dominio) < 3:
        return False
    
    if '.' not in correo:
        return False
    
    if ' ' in correo:
        return False
    
    if correo.startswith('.') or correo.endswith('.'):
        return False
    
    return True 
correo = input().strip()
print(es_correo_valido(correo))