import psycopg2

conexion = psycopg2.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_db')

# Corroboramos que llegamos a la conexión con un print que nos arroja un objeto
# print(conexion)

# Abrimos la BBDD para ver todo lo que hay en ella

try:
    with conexion.cursor() as cursor:
        sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
        #llaves_primarias = ((1,2,3,4),)
        entrada = input('Proporciona los id a buscar (separado por comas ","): ')
        # ahora hacemos .split(',') para sacar las comas
        # a la vez que convertimos a una tupla
        # y como es tupla de tuplas, los metemos en parentesis y 
        # la siguiente tupla no se pone nada
        llaves_primarias = (tuple(entrada.split(',')),)
        cursor.execute(sentencia,llaves_primarias)
        registros = cursor.fetchall()
        for registro in registros:
            print(registro)
except Exception as e:
    print(e)
finally:
    # Cerramos la conexión a la BBDD
    conexion.close()
