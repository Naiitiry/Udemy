"""
Ejercicio: Calculadora de Impuestos
Crear una función para calcular el total de un pago incluyendo un impuesto aplicado.
# Formula: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
"""

def calcu_imp(pago_sin_impuesto,impuesto):
    return pago_sin_impuesto + (pago_sin_impuesto * (impuesto/100))

print(calcu_imp(1000,16))