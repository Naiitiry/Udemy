class Producto:
    contador_productos = 0

    def __init__(self,nombre,precio):
        Producto.contador_productos += 1
        self._id_producto = Producto.contador_productos
        self._nombre = nombre
        self._precio = precio

    @property
    def precio(self):
        return self._precio
    
    def __str__(self):
        return f'Id Producto: {self._id_producto}, Nombre: {self._nombre}, Precio: {self._precio}'
    
    '''
    Es recomendable poner SETTER y GET para la modificación de los atributos 
    ya que los mismos están encapsulados.
    '''


if __name__ == '__main__':
    producto1 = Producto('Camisa',1000)
    print(producto1)
    producto2 = Producto('Remera', 500)
    print(producto2)