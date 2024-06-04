import os

class AgendaContactos:
    
    ruta_contactos = os.path.join(os.path.dirname(__file__),'data','contactos.txt')

    '''
    Para evitar poner en cada GIT PULL la nueva ruta para el
    archivo donde se guarda la información de los libros,
    con el módulo OS realizamos la manipulación de directorios
    y solucionamos, definitivamente, este contratiempo.
    '''
    
    @classmethod
    def verificar_directorio(cls):
        if not os.path.exists(os.path.dirname(cls.ruta_contactos)):
            os.makedirs(os.path.dirname(cls.ruta_contactos))

    @classmethod
    def agregar_contacto(cls,contacto):
        cls.verificar_directorio()
        with open(cls.ruta_contactos,'a',encoding='utf8') as archivo:
            archivo.write(f'{contacto.nombre},{contacto.apellido},{contacto.edad},{contacto.email},{contacto.telefono}\n')

    @classmethod
    def listar_contactos(cls):
        cls.verificar_directorio()
        try:
            with open(cls.ruta_contactos,'r',encoding='utf8') as archivo:
                contactos = archivo.readlines()
                if contactos:
                    print('\nContactos de la agenda:')
                    for contacto in contactos:
                        print(contacto.strip())
                else:
                    print('\nNo hay contactos.\n')
        except FileNotFoundError as f:
            print(f'\nNo existe el archivo con la lista de contactos.')
            print(f'Error: {f}')

    @classmethod
    def editar_contacto(cls,apellido,nuevo_mail,nuevo_telefono):
        cls.verificar_directorio()
        try:
            with open(cls.ruta_contactos,'r',encoding='utf8') as archivo:
                contactos = archivo.readlines()
            with open(cls.ruta_contactos,'w',encoding='utf8') as archivo:
                encontrado = False
                for contacto in contactos:
                    if contacto.split()[1] == apellido:
                        partes = contacto.strip().split(', ')
                        nombre = partes[0]
                        contacto_modificado = f'{nombre}, {apellido}, {nuevo_mail}, {nuevo_telefono}\n'
                        archivo.write(contacto_modificado)
                        encontrado = True
                    else:
                        archivo.write(contacto)
            if encontrado:
                print(f'El contacto con el apellido {apellido} ha sido modificado.')
            else:
                print(f'El contacto con el apellido {apellido} no se ha encontrado.')
        except FileNotFoundError as f:
            print('No se ha encontrado los contacto')
            print(f'Error: {f}')

    @classmethod
    def buscar_contacto(cls,apellido):
        cls.verificar_directorio()
        try:
            with open(cls.ruta_contactos,'r',encoding='utf8') as archivo:
                contactos = archivo.readlines()
                encontrado = False
                for contacto in contactos:
                    if contacto.strip()[1] == apellido:
                        print(f'Contacto encontrado: {contacto.strip()}')
                        encontrado = True
                        break
                if not encontrado:
                    print(f'El contacto con apellido {apellido}, no se encuentra en la agenda.')
        except FileNotFoundError as f:
            print(f'No se encontró contacto.')

    @classmethod
    def eliminar_contacto(cls,apellido):
        cls.verificar_directorio()
        try:
            with open(cls.ruta_contactos,'r') as archivo:
                contactos = archivo.readlines()
            with open(cls.ruta_contactos,'w',encoding='utf8') as archivo:
                encontrado = False
                for contacto in contactos:
                    if contacto.split()[1] == apellido:
                        encontrado = True
                    else:
                        archivo.write(contacto)
                if encontrado:
                    print(f'El contacto con el apellido {apellido} ha sido eliminado')
                else:
                    print(f'El contacto con el apellido {apellido} no ha sido encontrado')
        except FileNotFoundError as f:
            print('No se ha encontrado los contacto')
            print(f'Error: {f}')

    @classmethod
    def eliminar_archivo(cls):
        cls.verificar_directorio()
        os.remove(cls.ruta_contactos)
        print(f'Lista de contactos eliminada.')
