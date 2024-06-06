import psycopg2

conexion = psycopg2.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_db')

# Corroboramos que llegamos a la conexión con un print que nos arroja un objeto
# print(conexion)

# Abrimos la BBDD para ver todo lo que hay en ella

try:
    with conexion.cursor() as cursor:
        sentencia = 'SELECT * FROM persona WHERE id_persona = %s'

        # El '%s' es un placeholder, sirve para hacer referencia a 1 número
        # y no ponerlo manualmente y generar un input como abajo

        id_persona = input('Ingrese el id de la persona: ')
        # Luego debe pasarse dentro de execute como tupla, sino
        # arroja error en la búsqueda
        cursor.execute(sentencia,(id_persona,))
        # y ejecutamos fetchone para que traiga el 
        # registro específico y no todos y sobrecargue la memoria
        registro = cursor.fetchone()
        print(registro)
except Exception as e:
    print(e)
finally:
    # Cerramos la conexión a la BBDD
    conexion.close()
