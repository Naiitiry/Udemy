class Aritmetica:
    '''
    Clase aritmética para realizar sumas, resta, multiplicar, etc
    '''
    def __init__(self,operandoA,operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self):
        return self.operandoA + self.operandoB

    def restar(self):
        return self.operandoA - self.operandoB

    def multiplicar(self):
        return self.operandoA * self.operandoB

    def dividir(self):
        return self.operandoA / self.operandoB

artimetica1=Aritmetica(23,7)
print(f'La suma da como resultado: {artimetica1.sumar()}')
print(f'La resta da como resultado: {artimetica1.restar()}')
print(f'La multiplicación da como resultado: {artimetica1.multiplicar()}')
print(f'La división da como resultado: {artimetica1.dividir():.2f}')