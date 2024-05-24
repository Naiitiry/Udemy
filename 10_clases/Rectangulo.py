class Rectangulo:
    def __init__(self,ladoA,ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def area(self):
        return self.ladoA * self.ladoB
    
rectangulo1 = Rectangulo(25,15)
print(f'El área del rectángulo es: {rectangulo1.area()} metros cuadrados')