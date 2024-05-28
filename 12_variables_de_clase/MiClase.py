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
    
    # Clase 129 - Método de clase
    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

    # Clase 130 - contexto dinámico y estático
    def metodo_instacia(self):
        self.metodo_clase()
        self.metodo_estatico()

'''
print(MiClase.variable_clase) #Directamente de la clase.
miclase=MiClase('Valor variable instancia') # creamos la instancia.
print(miclase.variable_instancia)
print(miclase.variable_clase) # también se puede acceder desde el objeto.
'''
# clase 127
# Se puede crear variables de clase al vuelo (nuevas variables)

#MiClase.variable_clase2 = 'Nuevo valor variable clase 2'

# MiClase.metodo_estatico() #Accedemos al método estático

# MiClase.metodo_clase()
objeto1 = MiClase('Variable instancia')
objeto1.metodo_instacia() # Ejecuta 2 veces porque el método tiene 2 métodos más.
