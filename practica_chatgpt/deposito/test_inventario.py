from inventario.Inventario import Inventario as iv
from productos.Productos import Productos as ps

opcion = None
categoria_lista='snacks - verduleria - carniceria - congelados - lacteos - pastas - salsas - aderezos'

while opcion != 0:
    print('Bienvenido a La Amorosa'.center(50,'-'))
    print('Menú principal:')
    print('''
        1- Agregar producto
        \n2- Buscar producto
        \n3- Listar productos
        \n4- Modificar producto
        \n5- Eliminar producto
        \n6- Cerrar programa
        ''')
    opcion = int(input('Ingrese opción: '))
    if opcion == 1:
        categoria_producto = input(f'Ingrese la categoría {categoria_lista}: ')
        marca_producto = input('Ingrese marca del producto: ')
        nombre_producto = input('Ingrese nombre del producto: ')
        peso_producto = int(input('Ingrese peso del producto: '))
        precio_producto = float(input('Ingrese precio del producto: '))
        cantidad_producto = input('Ingrese cantidad del producto: ')
        varios = ps(categoria_producto,marca_producto,nombre_producto,peso_producto,precio_producto,cantidad_producto)
        iv.agregar_producto(varios)
        print('Producto agregado exitosamente.')
    elif opcion == 2:
        pass
    elif opcion == 3:
        print(iv.listar_producto())