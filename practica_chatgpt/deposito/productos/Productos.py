
class Productos:
    def __init__(self,categoria,marca,nombre,peso,precio,cantidad):
        self._categoria = categoria
        self._marca = marca
        self._nombre = nombre
        self._peso = peso
        self._precio = precio
        self._cantidad = cantidad
    
    def __str__(self):
        return f'Categoria: {self._categoria}, marca: {self._marca}, nombre: {self._nombre}, precio: {self._precio}, cantidad: {self._cantidad} y su peso: {self._peso}'
    
    # ********* GET Y SETTER *********

    '######################     GET     ######################'

    @property
    def categoria(self):
        return self._categoria

    @property
    def marca(self):
        return self._marca
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def peso(self):
        return self._peso
    
    @property
    def precio(self):
        return self._precio
    
    @property
    def cantidad(self):
        return self._cantidad
    
    '######################     SETTER     ######################'

    @categoria.setter
    def categoria(self,categoria):
        self._categoria = categoria
    
    @marca.setter
    def marca(self,marca):
        self._marca = marca

    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre
    
    @peso.setter
    def peso(self,peso):
        self._peso = peso
    
    @precio.setter
    def precio(self,precio):
        self._precio = precio
    
    @cantidad.setter
    def cantidad(self,cantidad):
        self._cantidad = cantidad
    