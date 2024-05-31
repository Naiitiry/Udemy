# Clase 155
try:
    archivo = open('C:/Users/rdanchuk/Desktop/Python/Udemy/20_archivos/prueba.txt','w',encoding='utf8')
    #el UTF8 permite que ponga acentos
    archivo.write('Agregamos información al archivo\n')
    archivo.write('Adiosito')
except Exception as e:
    print(e)
finally:
    archivo.close()