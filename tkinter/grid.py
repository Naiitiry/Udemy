from tkinter import *
from tkinter import ttk

ventana = Tk()
ventana.geometry('600x400')
ventana.title('Grid')
ventana.iconbitmap('C:/Users/rdanchuk/Desktop/Python/Udemy/tkinter/icono.ico')

def evento_1():
    boton1.config(text='Botón 1 presionado')

def evento_2():
    boton2.config(text='Botón 2 presionado')

boton1 = ttk.Button(ventana,text='Botón 1',command=evento_1)
boton1.grid(row=0,column=0,sticky='WE')

boton2 = ttk.Button(ventana,text='Botón 2',command=evento_2)
boton2.grid(row=1,column=0,sticky='E')



ventana.mainloop()