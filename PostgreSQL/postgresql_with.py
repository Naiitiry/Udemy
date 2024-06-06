import psycopg2

conexion = psycopg2.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_db')

# Corroboramos que llegamos a la conexión con un print que nos arroja un objeto
# print(conexion)

# Abrimos la BBDD para ver todo lo que hay en ella

try:
    with conexion.cursor() as cursor:
        sentencia = 'SELECT * FROM persona'
        cursor.execute(sentencia)
        registro = cursor.fetchall()
        print(registro)
except Exception as e:
    print(e)
finally:
    # Cerramos la conexión a la BBDD
    conexion.close()
