import psycopg2

conexion = psycopg2.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_db')

# Corroboramos que llegamos a la conexión con un print que nos arroja un objeto
# print(conexion)

# Abrimos la BBDD para ver todo lo que hay en ella

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email=%s WHERE id_persona=%s'
            valores = (
                ('Juan','Perez','jperez@gmail.com',1),
                ('María','García','no posee',2),
                )
            cursor.executemany(sentencia, valores)
            registros_actualizados = cursor.rowcount
            print(f'Registros actualizados: {registros_actualizados}')
except Exception as e:
    print(e)
finally:
    # Cerramos la conexión a la BBDD
    conexion.close()
