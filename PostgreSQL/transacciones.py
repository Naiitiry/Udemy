# Clase 181

import psycopg2 as bd

conexion = bd.connect(user='postgres1',password='admin',host='127.0.0.1',port='5432',database='test_db')

# Corroboramos que llegamos a la conexión con un print que nos arroja un objeto
# print(conexion)

# Abrimos la BBDD para ver todo lo que hay en ella

try:
    conexion.autocommit = False
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre,apellido,email) VALUES(%s,%s,%s)'
    valores=(('Maria','Aguirre','maagui@gmail.com'),)
    cursor.execute(sentencia,valores)
    conexion.commit()
    print('Termina la transacción.')
except Exception as e:
    conexion.rollback()
    print(e)
finally:
    # Cerramos la conexión a la BBDD
    conexion.close()
