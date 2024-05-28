'''
Clase Biblioteca
Atributos:

nombre (string)
libros (lista de objetos Libro)
usuarios (lista de objetos Usuario)
Métodos:

__init__(self, nombre): inicializa los atributos de la biblioteca.
    agregar_libro(self, libro): agrega un libro a la biblioteca.
    registrar_usuario(self, usuario): registra un usuario en la biblioteca.
    prestar_libro(self, id_usuario, id_libro): presta un libro a un usuario si está disponible.
    devolver_libro(self, id_usuario, id_libro): el usuario devuelve un libro a la biblioteca.
__str__(self): representa la biblioteca como una cadena de texto, 
    mostrando los libros disponibles y los usuarios registrados.
'''

class Biblioteca:
    def __init__(self):
        pass