class Contactos:
    
    def __init__(self,nombre,apellido,edad,email,telefono):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        self._email = email
        self._telefono = telefono

    def __str__(self):
        return f'Nombre: {self._nombre}, apellido: {self._apellido}, edad: {self._edad}, email: {self._email}, teléfono: {self._telefono}'
    
    # Métodos de GET y SETTER

    # GET

    @property
    def nombre(self):
        return self._nombre
    
    @property
    def apellido(self):
        return self._apellido
    
    @property
    def edad(self):
        return self.edad
    
    @property
    def email(self):
        return self._email
    
    @property
    def telefono(self):
        return self._telefono
    
    # SETTER

    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre

    @apellido.setter
    def apellido(self,apellido):
        self._apellido = apellido

    @edad.setter
    def edad(self,edad):
        self._edad = edad

    @email.setter
    def email(self,email):
        self._email = email

    @telefono.setter
    def telefono(self,telefono):
        self._telefono = telefono