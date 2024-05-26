#ABC = Abstract Base Class - Abstracción de Clase - Video 125
#from abc import ABC,classmethod

class FiguraGeometrica2():
    def __init__(self,alto,ancho):
        self._alto = alto
        self._ancho = ancho
    
    # Estoy creando los get para los datos de alto y ancho
    @property
    def alto(self):
        return self._alto
    
    @property
    def ancho(self):
        return self._ancho
    
    # Ahora estoy aplicando Setters para modificar dicha variable
    @alto.setter
    def alto(self,alto):
        self._alto = alto

    @ancho.setter
    def ancho(self,ancho):
        self._ancho = ancho
    
    @classmethod
    def calculr_area(self):
        pass

    def __str__(self):
        return f'La figura tiene {self.alto} de alto x {self.ancho} de ancho'

if __name__ == '__main__':
    locura = FiguraGeometrica2(3,6)
    print(locura)

    print(__name__)