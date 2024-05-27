# Clase 126
class MiClase:
    variable_clase = 'Valor variable clase'

    def __init__(self,variable_instancia):
        self.variable_instancia = variable_instancia

    #clase 128 - Metodo estático

    @staticmethod
    #No puede acceder al atributo o variable de instancia.
    #Pero si a la de clase, pero no directamente.
    def metodo_estatico():
        print(MiClase.variable_clase)

'''
print(MiClase.variable_clase) #Directamente de la clase.
miclase=MiClase('Valor variable instancia') # creamos la instancia.
print(miclase.variable_instancia)
print(miclase.variable_clase) # también se puede acceder desde el objeto.
'''
# clase 127
# Se puede crear variables de clase al vuelo (nuevas variables)

MiClase.variable_clase2 = 'Nuevo valor variable clase 2'

MiClase.metodo_estatico() #Accedemos al método estático