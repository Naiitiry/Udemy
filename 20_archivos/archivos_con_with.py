# 159 - Manejo de archivos con WITH

# with open('C:/Users/rdanchuk/Desktop/Python/Udemy/20_archivos/prueba.txt','r',encoding='utf8') as archivo:
#     print(archivo.read())

# Utilizamos la clase creada ManejoArchivos
from ManejoArchivos import *

with ManejoArchivos('C:/Users/rdanchuk/Desktop/Python/Udemy/20_archivos/prueba.txt') as archivo:
    print(archivo.read())
