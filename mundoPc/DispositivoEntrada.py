class DispositivoEntrada:
    def __init__(self,tipo_entrada,marca):
        self._tipo_entrada = tipo_entrada
        self._marca = marca
    
    @property
    def tipo_entrada(self):
        pass

    def __str__(self):
        return f''