from Biblioteca import *
from Libro import *
from Usuario import *

# Crear Libro
libro1 = Libro('Los arboles mueren de pie',"Nico Vazquez",1997)

# Creamos al usuario
usuario1 = Usuario('Nicolas')

biblioteca1 = Biblioteca('Biblioteca Central')

biblioteca1.agregar_libro(libro1)

biblioteca1.registrar_usuario(usuario1)

print(biblioteca1)