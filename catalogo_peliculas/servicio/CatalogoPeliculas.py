import os

class CatalogoPeliculas:
    ruta_archivo = '../peliculas.txt'

    @classmethod
    def agregar_pelicula(cls,pelicula):
        with open(cls.ruta_archivo,'a',encoding='utf8') as archivo:
            archivo.write(f'{pelicula.nombre}\n')

    @classmethod
    def listar_peliculas(cls):
        with open(cls.ruta_archivo,'r',encoding='utf8') as archivo:
            print('\n'+' Catalogo de peliculas '.center(50,'-')+'\n')
            print(archivo.read())

    @classmethod
    def eliminar_peliculas(cls):
        os.remove(cls.ruta_archivo)
        print(f'Archivo eliminado {cls.ruta_archivo}')
