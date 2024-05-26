from FiguraGeometrica2 import *
from Color2 import *

class Rectangulo2(FiguraGeometrica2,Color2):
    def __init__(self,alto,ancho,color):
        #super().__init__(alto, ancho)
        FiguraGeometrica2.__init__(self,ancho,alto)
        Color2.__init__(self,color)

    def calcular_area(self):
        return self.alto * self.ancho
    
    def __str__(self):
        return f'[Soy la clase Padre FiguraGeometrica2: {FiguraGeometrica2.__str__(self)}] \n[Soy la clase Padre Color2: {Color2.__str__(self)}]'