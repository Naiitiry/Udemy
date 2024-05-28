'''
Clase Usuario
Atributos:

nombre (string)
id_usuario (int, autoincremental)
libros_prestados (lista de objetos Libro)

Métodos:
__init__(self, nombre): inicializa los atributos del usuario.
    prestar_libro(self, libro): agrega un libro a la lista de libros prestados del usuario.
    devolver_libro(self, libro): elimina un libro de la lista de libros prestados del usuario.
__str__(self): representa el usuario como una cadena de texto.
'''

class Usuario:
    contador_usuarios = 0
    def __init__(self,nombre,libros_prestados):
        Usuario.contador_usuarios += 1
        self._id_usuario = Usuario.contador_usuarios
        self._nombre = nombre
        self._libros_prestados = []
    
    def prestar_libro(self,libro):
        self._libros_prestados.append(libro)

    def devolver_libro(self,libro):
        self._libros_prestados.remove(libro)

    def __str__(self):
        libros_prestados_str=', '.join([libro._titulo for libro in self._libros_prestados])
        return f'ID Usuario: {self._id_usuario}, Nombre: {self._nombre}, Libros prestados: {self._libros_prestados}'
