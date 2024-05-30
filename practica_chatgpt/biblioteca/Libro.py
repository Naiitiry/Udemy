'''
Clase Libro
Atributos:

titulo (string)
autor (string)
anio (int)
id_libro (int, autoincremental)
disponible (bool, inicialmente True)

Métodos:
__init__(self, titulo, autor, anio): inicializa los atributos del libro.
__str__(self): representa el libro como una cadena de texto.
'''

class Libro:
    contador_libros = 0
    def __init__(self,titulo,autor,anio):
        Libro.contador_libros += 1
        self._id_libro = Libro.contador_libros
        self._titulo = titulo
        self._autor = autor
        self._anio = anio
        self.disponible = True

    def __str__(self):
        estado = 'Disponible' if self.disponible else 'Prestado'
        return f'ID: {self._id_libro}, Libro: {self._titulo}, Autor: {self._autor}, Año de publicación: {self._anio}, Disponibilidad: {estado}'
