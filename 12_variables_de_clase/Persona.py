# Clase 132 - contador de objetos creados

class Persona:
    contador_persona = 0

    # Clase 133 - Mejora del contador.
    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_persona += 1
        return cls.contador_persona 

    def __init__(self,nombre,edad):
        self.id_persona = Persona.generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona: {self.id_persona}, {self.nombre} y {self.edad} años'
    
persona1 = Persona('Juan',33)
print(persona1)
persona2 = Persona('Agustina', 22)
print(persona2)