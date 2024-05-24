"""
Ejercicio: Convertidor de Temperatura
Realizar dos funciones para convertir de grados celsius a fahrenheit y viceversa.
"""
def conversor_temp_c_a_f(celcius):
    return (celcius*(9/5))+32

def conversor_temp_f_a_c(faren):
    return (faren-32)*(5/9)

print(f'{conversor_temp_c_a_f(25):.2f}')
print(f'{conversor_temp_f_a_c(75):.2f}')