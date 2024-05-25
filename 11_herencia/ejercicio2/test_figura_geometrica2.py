from Cuadrado2 import *

cuadrado2 = Cuadrado2(6,'Verde')

# Llama la clase Cuadrado2 el __str__ modificado a las clases padres
print(f'El área es de {cuadrado2.calcular_area()} unidades.')

# muestra lo que vemos de las clases padres FiguraGeometrica2 y Color2
print(cuadrado2) 