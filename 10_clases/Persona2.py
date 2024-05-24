class Persona2():
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona: {self.nombre} de {self.edad} años'


class Empleado(Persona2):
    def __init__(self,nombre,edad,sueldo):
        super().__init__(nombre,edad)
        self.sueldo = sueldo
    
    def __str__(self):
        return f'con un sueldo de: {self.sueldo} {super().__str__()} '
