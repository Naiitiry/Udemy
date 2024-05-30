from DispositivoEntrada import *

class Monitor(DispositivoEntrada):
    contador_monitor = 0
    def __init__(self, tipo_entrada, marca,tamanio):
        super().__init__(tipo_entrada, marca)
        Monitor.contador_monitor += 1
        self._id_monitor = Monitor.contador_monitor
        self._tamanio = tamanio

    def __str__(self):
        return f'ID: {self._id_monitor}, Marca: {self._marca}, Tipo_entrada: {self._tipo_entrada}, Tamaño: {self._tamanio}'


if __name__ == '__main__':
    pass
    # monitor1 = Monitor('USB','Samsung','17"')
    # print(monitor1)
    # monitor2 = Monitor('USB','Samsung','17"')
    # print(monitor2)