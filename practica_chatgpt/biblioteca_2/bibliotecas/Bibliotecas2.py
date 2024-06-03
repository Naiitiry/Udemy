import os

class Biblioteca2:

    # Disponemos del archivo .txt con una ruta de acceso
    # con el módulo os

    ruta_libros = os.path.join(os.path.dirname(__file__),'data','libros.txt')

    '''
    Para evitar poner en cada GIT PULL la nueva ruta para el
    archivo donde se guarda la información de los libros,
    con el módulo OS realizamos la manipulación de directorios
    y solucionamos, definitivamente, este inconveniente.
    '''

    @classmethod
    def verificar_directorio(cls):
        if not os.path.exists(os.path.dirname(cls.ruta_libros)):
            os.makedirs(os.path.dirname(cls.ruta_libros))

    @classmethod
    def agregar_libro(cls,libro):
        cls.verificar_directorio()
        with open(cls.ruta_libros,'a',encoding='utf8') as archivo:
            archivo.write(f'{libro.titulo},{libro.autor},{libro.editorial},{libro.anio}\n')
    
    @classmethod
    def listar_libros(cls):
        cls.verificar_directorio()
        with open(cls.ruta_libros,'r',encoding='utf8') as archivo:
            print('\n-'.center(50,'-'))
            print('Libros'.center(50,'-'))
            print('-'.center(50,'-')+'\n')
            print(archivo.read())
    

    @classmethod
    def eliminar_libros(cls):
        cls.verificar_directorio()
        os.remove(cls.ruta_libros)
        print(f'\nArchivo de libros Eliminado {cls.ruta_libros}\n')