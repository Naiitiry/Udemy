ruta = 'C:\\Users\\rdanchuk\\Desktop\\Python\\Udemy\\20_archivos\\prueba.txt'
archivo=open(ruta,'r',encoding='utf8')
# print(archivo.read())

# leer algunos caracteres
# print(archivo.read(5))

# Leer lineas
# print(archivo.readline())
# print('**************************')
# print(archivo.readline())

# iterar archivo
# for line in archivo:
#     print(line)

# Leer todas las líneas con 1 método
# todo en 1 lista
# print(archivo.readlines())

# Acceder a 1 linea de la lista
# print(archivo.readlines()[1])

# Crear copia del archivo original
# a - para anexar información
archivo2 = open('C:/Users/rdanchuk/Desktop/Python/Udemy/20_archivos/copia.txt','a',encoding='utf8')
archivo2.write(archivo.read())

archivo.close()
archivo2.close()
print('Se terminó el copiado de archivos.')