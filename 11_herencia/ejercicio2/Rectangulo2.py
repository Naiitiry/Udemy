from FiguraGeometrica2 import *
from Color2 import *

class Rectangulo2(FiguraGeometrica2,Color2):
    def __init__(self, alto, ancho):
        super().__init__(alto, ancho)