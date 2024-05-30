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
    pass
    # teclado1 = Teclado('USB','Hp')
    # raton1 = Raton('Wireless','Hp')
    # monitor1 = Monitor('HDMI','Hp','50"')
    # computadora1 = Computadora('HP',monitor1,teclado1,raton1)
    # print(computadora1)
    
    # teclado2 = Teclado('Wireless','Razer')
    # raton2 = Raton('Wireless/C','Razer')
    # monitor2 = Monitor('HDMI','Razer','32"')
    # computadora2 = Computadora('Razer',monitor2,teclado2,raton2)
    # print(computadora2)