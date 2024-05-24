def listar_terminos(**terminos):
    for llave,valor in terminos.items():
        print(f'{llave}: {valor}')

listar_terminos(IDE='Integrated Development Enviroment',PK='Primary Key')