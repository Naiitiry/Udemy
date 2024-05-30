from Teclado import *
from Raton import *
from Monitor import *

class Computadora:
    contador_computadora = 1000
    def __init__(self,nombre,monitor,teclado,raton):
        Computadora.contador_computadora += 1
        self._id_computadora = Computadora.contador_computadora
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        return f'''
        {self._nombre}: ID {self._id_computadora}
        Monitor: {self._monitor}
        Teclado: {self._teclado}
        Ratón: {self._raton}
        '''


if __name__ == '__main__':
    teclado1 = Teclado('USB','Hp')
    raton1 = Raton('Wireless','Razer')
    monitor1 = Monitor('HDMI','Loginius','50"')
    computadora1 = Computadora('Caso 1',monitor1,teclado1,raton1)
    print(computadora1)