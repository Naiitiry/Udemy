import psycopg2

conexion = psycopg2.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_db')

# Corroboramos que llegamos a la conexión con un print que nos arroja un objeto
# print(conexion)

# Abrimos la BBDD para ver todo lo que hay en ella

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE FROM persona WHERE id_persona = %s'
            # debe ingresarse una tupla, por la sentencia %s
            valores = (8,)
            cursor.execute(sentencia,valores)
            registros_eliminados = cursor.rowcount
            print(f'Registros eliminados: {registros_eliminados}')
except Exception as e:
    print(e)
finally:
    # Cerramos la conexión a la BBDD
    conexion.close()

# Para eliminar varios registros, mirar como se utiliza en postgresql_with_3
# es lo mismo pero solo con DELETE FROM y en valores se utiliza (tuple(entrada.split(",")),)
# siendo que la entrada es un input que pide id_persona separados con ",".