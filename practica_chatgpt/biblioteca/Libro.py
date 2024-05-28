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
        self._disponible = True
    
    # Aplicamos Setter y Get a la Clase Disponible
    # GET
    @property
    def disponible(self):
        return self._disponible
    
    # SETTER
    @disponible.setter
    def disponible(self,disponible):
        self._disponible = disponible

    def __str__(self):
        return f'ID: {self._id_libro}, Libro: {self._titulo}, Autor: {self._autor}, Año de publicación: {self._anio}, Disponibilidad: {self.disponible}'

if __name__ == "__main__":
    libro1 = Libro('Los arboles mueren de pie',"Nico Vazquez",1997)
    print(libro1)