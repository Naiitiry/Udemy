from Producto import *
from Orden import *


producto1 = Producto('Camisa',1000)
producto2 = Producto('Remera', 500)
producto3 = Producto('Jean', 2500)
producto4 = Producto('Riñonera',7500)
producto5 = Producto('Medias',700)


productos1 = [producto1,producto2]
productos2 = [producto3,producto5]
productos3 = [producto4,producto1]


orden1 = Orden(productos1)
orden1.agregar_producto(producto3)

orden2 = Orden(productos2)
orden2.agregar_producto(producto4)

orden3 = Orden(productos3)
orden3.agregar_producto(producto1)
orden3.agregar_producto(producto4)

print(orden1)
print(f'El total es: {orden1.calcular_total()}')
print(orden2)
print(f'El total es: {orden2.calcular_total()}')
print(orden3)
print(f'El total es: {orden3.calcular_total()}')