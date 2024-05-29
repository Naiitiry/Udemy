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
    def __init__(self,nombre,):
        self._nombre = nombre
        self._libros = []
        self._usuarios = []
    
    def agregar_libro(self,libro):
        self._libros.append(libro)

    def registrar_usuario(self,usuario):
        self._usuarios.append(usuario)

    def prestar_libro(self,id_usuario,id_libro):
        usuario = None
        libro = None

        #Busca el usuario por id_usuario
        for u in self._usuarios:
            if u._id_usuario == id_usuario:
                usuario = u
                break

        # Busca el libro por id_libro
        for l in self._libros:
            if l._id_libro == id_libro:
                libro = l
                break
        
        # Comparamos ambas busquedas
        if usuario is not None and libro is not None:
            libro.disponible = False
            usuario.prestar_libro(libro)
            print(f'El libro {libro._titulo} fue prestado a {usuario._nombre}')
        else:
            print('No se pudo prestar')

    def devolver_libro(self,id_usuario,id_libro):
        usuario = None
        libro = None
        #Busca el usuario por id_usuario
        for u in self._usuarios:
            if u._id_usuario == id_usuario:
                usuario = u
                break
        
        for l in self._libros:
            if l._id_libro == id_libro:
                libro = l
                break
        
        # Comparamos ambas busquedas
        if usuario is not None and libro is not None:
            libro.disponible = True
            usuario.prestar_libro(libro)
            print(f'El libro {libro._titulo} fue devuelto por {usuario._nombre}')
        else:
            print('No se pudo devolver el libro')

    def __str__(self):
        libro_str = ''
        for libro in self._libros:
            libro_str += libro.__str__() + '\n'

        usuario_str = ''
        for usuario in self._usuarios:
            usuario_str += usuario.__str__() + '\n'
