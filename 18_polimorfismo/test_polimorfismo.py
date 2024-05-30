from Empleado import *
from Gerente import *

def mostrar_detalle(objeto):
    print(objeto) #acá se aplica el concepto de POLIMORFISMO
    print(type(objeto))
    # Clase 142 - isinstance()
    if isinstance(objeto, Gerente):
        print(f'El atributo dentro de la clase gerente son: {objeto.departamento}')

empleado = Empleado('Juan',5000)
mostrar_detalle(empleado)

gerente = Gerente('Carla',8000,'RRHH')
mostrar_detalle(gerente)