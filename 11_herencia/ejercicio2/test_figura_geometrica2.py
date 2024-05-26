from Cuadrado2 import *
from Rectangulo2 import *

#No se puede instanciar una clase abstracta.
#figura = FiguraGeometrica2()

cuadrado2 = Cuadrado2(6,'Verde')
print('Creación Objeto Cuadrado'.center(50,'*'))

# Llama la clase Cuadrado2 el __str__ modificado a las clases padres
print(f'\nEl área del cuadrado es de {cuadrado2.calcular_area()} unidades.')

# muestra lo que vemos de las clases padres FiguraGeometrica2 y Color2
print(str(cuadrado2)+'\n') 


rectangulo2 = Rectangulo2(5,6,'Naranja')
print('Creación Objeto Rectangulo'.center(50,'*'))
# Llama la clase Rectangulo2 el __str__ modificado a las clases padres
print(f'\nEl área del rectángulo es de {rectangulo2.calcular_area()} unidades.')

# muestra lo que vemos de las clases padres FiguraGeometrica2 y Color2
print(rectangulo2) 