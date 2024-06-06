import psycopg2

conexion = psycopg2.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_db')

# Corroboramos que llegamos a la conexión con un print que nos arroja un objeto
# print(conexion)

# Abrimos la BBDD para ver todo lo que hay en ella

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "INSERT INTO persona(nombre,apellido,email) VALUES(%s, %s, %s)"
            valores = ('Carlos','Lara','clara@gmail.com')
            cursor.execute(sentencia, valores)
            # se deben guardar con la siguiente sentencia
            # conexion.commit()
            # pero al utilizar WITH ya lo hace automáticamente
            registros_insertados = cursor.rowcount
            print(f'Registros ingresados: {registros_insertados}')
except Exception as e:
    print(e)
finally:
    # Cerramos la conexión a la BBDD
    conexion.close()
