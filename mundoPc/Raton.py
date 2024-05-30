from DispositivoEntrada import *

class Raton(DispositivoEntrada):
    contador_raton = 0
    def __init__(self, tipo_entrada, marca):
        super().__init__(tipo_entrada, marca)
        Raton.contador_raton += 1
        self._id_raton = Raton.contador_raton

    def __str__(self):
        return f'ID: {self._id_raton}, Marca: {self._marca}, Tipo_entrada: {self._tipo_entrada}'


if __name__ == "__main__":
    pass
    # raton1 = Raton('Hp','USB')
    # print(raton1)
    # raton2 = Raton('Acer','USB/Bloothot')
    # print(raton2)