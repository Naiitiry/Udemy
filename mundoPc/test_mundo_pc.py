from Raton import *
from Teclado import *
from Monitor import *
from Computadora import *
from Orden import *

teclado1 = Teclado('USB','Hp')
raton1 = Raton('Wireless','Hp')
monitor1 = Monitor('HDMI','Hp','50"')
computadora1 = Computadora('HP',monitor1,teclado1,raton1)
#print(computadora1)
    
teclado2 = Teclado('Wireless','Razer')
raton2 = Raton('Wireless/C','Razer')
monitor2 = Monitor('HDMI','Razer','32"')
computadora2 = Computadora('Razer',monitor2,teclado2,raton2)
#print(computadora2)

computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)
orden1.agregar_computadora(computadoras1)
print(orden1)
