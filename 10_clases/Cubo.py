class Cubo():
    def __init__(self,ancho,alto,profundo):
        self.ancho = ancho
        self.alto = alto
        self.profundo = profundo

    def volumen(self):
        return self.ancho * self.alto * self.profundo


ancho= float(input('Ingrese el ancho: '))
alto= float(input('Ingrese el alto: '))
profundo= float(input('Ingrese el profundo: '))
cubo1 = Cubo(ancho,alto,profundo)
print(f'El volúmen del cubo es de: {cubo1.volumen()}')