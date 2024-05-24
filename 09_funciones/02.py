# Si a la varibale la declaramos con valores, no va a dar problemas
'''
def sumar(a=0,b=0):
    return a + b

resultado = sumar(8)
print(f'\nEl resultado es: {resultado}')
'''

def listar_nombres(*nombres):
    for nombre in nombres:
        print(nombre)

listar_nombres('Hernesto','Penelope','Timoteo','Agostina')