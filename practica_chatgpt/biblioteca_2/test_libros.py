from libros.Libros2 import Libros2
from bibliotecas.Bibliotecas2 import Biblioteca2 as bi

opcion = None

while opcion != 4:
    print(' Bienvenido a Biblioteca La Cardeus '.center(50,'-'))
    print('\nSeleccione alguna de las siguientes opciones:')
    print('''
            \n1- Agregar libro
            \n2- Listar libros
            \n3- Eliminar archivo de libros
            \n4- Salir
            ''')
    opcion = int(input('Ingrese su opción: '))
    if opcion == 1:
        titulo_libro = input('Ingrese título del libro: ')
        autor_libro = input('Ingrese autor del libro: ')
        editorial_libro = input('Ingrese editorial del libro: ')
        anio_libro = input('Ingrese año del libro: ')
        varios = Libros2(titulo_libro,autor_libro,editorial_libro,anio_libro)
        bi.agregar_libro(varios)
        print('Libro agregado exitosamente!')
    elif opcion == 2:
        try:
            bi.listar_libros()
        except Exception as e:
            print(f'Lista aún no creada, error: {e}')
    elif opcion == 3:
        try:
            bi.eliminar_libros()
        except Exception as e:
            print(f'Lista aún no creada, error: {e}')
    else:
        print(' Que tengas buen día '.center(50,'*'))
        break
