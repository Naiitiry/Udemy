from DispositivoEntrada import * 

class Teclado(DispositivoEntrada):
    contador_teclado = 0
    def __init__(self, tipo_entrada, marca):
        super().__init__(tipo_entrada, marca)
        Teclado.contador_teclado += 1
        self._id_teclado = Teclado.contador_teclado
    
    def __str__(self):
        return f'ID: {self._id_teclado}, Marca: {self._marca}, Tipo_entrada: {self._tipo_entrada}'


if __name__ == '__main__':
    pass
    # teclado1 = Teclado('R2','Genius')
    # print(teclado1)
    # teclado2 = Teclado('USB/Wireless','Hp')
    # print(teclado2)