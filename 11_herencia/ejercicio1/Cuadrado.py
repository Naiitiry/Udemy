from FiguraGeometrica import *
from Color import *

class Cuadrado(FiguraGeometrica,Color):
    def __init__(self, lado,color):
        #super().__init__(lado)
        FiguraGeometrica.__init__(self,lado,lado)
        Color.__init__(self,color)
    
    def calcular_area(self):
        return self.alto * self.ancho
    
