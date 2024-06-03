#  Clase - 169

# Instalar módulo para conectar pstgresql

# pip install psycopg2

import psycopg2

conexion = psycopg2.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_db')

# Corroboramos que llegamos a la conexión con un print que nos arroja un objeto
# print(conexion)

# Abrimos la BBDD para ver todo lo que hay en ella

cursor = conexion.cursor()
sentencia = 'SELECT * FROM persona'
cursor.execute(sentencia)
registro = cursor.fetchall()
print(registro)


# Cerramos la BBDD
cursor.close()
conexion.close()