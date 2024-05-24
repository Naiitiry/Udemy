"""
Crear una función para sumar los valores recibidos de tipo numérico, 
utilizando argumentos variables *args como parámetro de la función 
y regresar como resultado la suma de todos los valores pasados como argumentos.
"""

def sumar(*args):
    suma=0
    for valor in args:
        suma += valor
    return suma

print(sumar(7,8,9,5,3,6,7,1,456))