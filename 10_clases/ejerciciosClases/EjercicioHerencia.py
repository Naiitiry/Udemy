"""
Definir una clase padre llamada Vehiculo y dos clases hijas llamadas Coche y Bicicleta,
las cuales heredan de la clase Padre Vehiculo.
La clase padre debe tener los siguientes atributos y métodos

Vehiculo (Clase Padre):
-Atributos (color, ruedas)
-Métodos ( __init__() y __str__ )

Coche  (Clase Hija de Vehículo) (Además de los atributos y métodos heradados de Vehículo):
-Atributos ( velocidad (km/hr) )
-Métodos ( __init__() y __str__() )

Bicicleta  (Clase Hija de Vehículo) (Además de los atributos y métodos heradados de Vehículo):
-Atributos ( tipo (urbana/montaña/etc )
-Métodos ( __init__() y __str__() )
"""

class Vehiculo():
    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        # return f'Vehiculo de color {self.color} con {self.ruedas} ruedas'
        # la siguiente manera lo hace el profe
        return 'Color: ' + self.color + ', Ruedas: '+ str(self.ruedas)

class Coche(Vehiculo):
    def __init__(self, color, ruedas,velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return f'{super().__str__()}, velocidad de: {self.velocidad} km/hr'

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas,tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    
    def __str__(self):
        return f'{super().__str__()} bicicleta tipo {self.tipo} '
    

#vehiculo1 = Vehiculo('verde',4)
#print(vehiculo1)

#bici1 = Bicicleta('rojo',3,'montaña')
#print(bici1)

#coche1 = Coche('naranja',6,65)
#print(coche1)