from agenda_contactos.AgendaContactos import AgendaContactos as ag
from contactos.Contactos import Contactos as co

opcion = None

while opcion != 7:
    print('Bienvenido a su agenda personal')
    print('Seleccione una de las siguientes opciones:')
    print('1- Agregar contacto\n2- Buscar contacto\n3- Editar contacto\n4- Eliminar contacto\n5- Listar contactos\n6- Eliminar lista de contactos\n7- Salir.')
    opcion = int(input('Ingrese opción: '))
    if opcion == 1:
        nombre = input('Ingrese nombre del contacto: ')
        apellido = input('Ingrese apellido del contacto: ')
        edad = input('Ingrese edad: ')
        email = input('Ingrese E-mail del contacto: ')
        telefono = input('Ingrese teléfono: ')
        varios = co(nombre,apellido,edad,email,telefono)
        ag.agregar_contacto(varios)
        print('Usuario agendado exitosamente!')
    elif opcion == 2:
        apellido2 = input('Ingrese el apellido a buscar: ')
        ag.buscar_contacto(apellido2)
    elif opcion == 3:
        editar_apellido = input('Ingrese el apellido del contacto a editar: ')
        editar_telefono = int(input('Ingrese el telefono nuevo: '))
        editar_email = input('Ingrese el mail nuevo: ')
        ag.editar_contacto(editar_apellido,editar_telefono,editar_email)
    elif opcion == 4:
        eliminar_apellido = input('Ingrese apellido de contacto a eliminar: ')
        ag.eliminar_contacto(eliminar_apellido)
    elif opcion == 5:
        ag.listar_contactos()
    elif opcion == 6:
        ag.eliminar_archivo()
    else:
        print('Que tengas buen día!')
