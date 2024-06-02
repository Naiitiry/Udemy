class Libros2:

    def __init__(self,titulo,autor,anio,editorial):
        self._titulo = titulo
        self._autor = autor
        self._anio = anio
        self._editorial = editorial
    
    def __str__(self):
        return f'Libro: {self._titulo},Autor: {self._autor},Editorial: {self._editorial},Año: {self._anio}\n'

    # Realizamos los SETTER y GET correspondientes

    ############################################
    # Realizamos los GET de todos los atributos.
    ############################################

    @property
    def titulo(self):
        return self._titulo
    
    @property
    def autor(self):
        return self._autor
    
    @property
    def anio(self):
        return self._anio
    
    @property
    def editorial(self):
        return self._editorial
    
    ###############################################
    # Realizamos todos los SETTER de los atributos.
    ###############################################

    @titulo.setter
    def titulo(self,titulo):
        self._titulo = titulo
    
    @autor.setter
    def autor(self,autor):
        self._autor = autor

    @anio.setter
    def anio(self,anio):
        self._anio = anio
    
    @editorial.setter
    def editorial(self,editorial):
        self._editorial = editorial