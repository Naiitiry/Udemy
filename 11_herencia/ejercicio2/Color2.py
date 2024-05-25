class Color2:
    def __init__(self,color):
        self._color = color
    
    # Aplicamos Setter y Get a la Clase Color
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self,color):
        self._color = color
    
    def __str__(self):
        return f'Color: {self.color}'