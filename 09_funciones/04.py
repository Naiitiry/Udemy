"""
Crear una función para multiplicar los valores recibidos de tipo numérico,
utilizando argumentos variables *args como parámetro de la función
y regresar como resultado la multiplicación de todos los valores pasados como argumentos.
"""
def multiplicar(*args):
    multi=1
    for valor in args:
        multi *= valor
    return multi

print(f'Resultado: {multiplicar(7,6,3,5)}')