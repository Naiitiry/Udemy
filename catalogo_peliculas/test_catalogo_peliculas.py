from dominio.Pelicula import Pelicula as pe
from servicio.CatalogoPeliculas import CatalogoPeliculas as cp

opcion = None

while opcion != 4:
        print(" Bienvenido a PeliPedia ".center(50,'#'))
        print('\nSelecciones una opcion')
        print("\n1- Agregar pelicula\n2- Listar pelicula\n3- Eliminar archivo\n4- Salir: ")
        opcion = int(input('Ingrese aquí su selección: '))
        if opcion == 1:
            nombre_pelicula = input('Ingresa el nombre de la pelicula: ')
            pelicula = pe(nombre_pelicula)
            cp.agregar_pelicula(pelicula)
        elif opcion == 2:
            cp.listar_peliculas()
        elif opcion == 3:
            print('Se eliminará el archivo de peliculas')
            cp.eliminar_peliculas()
        else:
            print(' Que tengas buen día '.center(50,'*'))
            break