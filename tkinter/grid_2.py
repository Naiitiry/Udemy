from tkinter import *
from tkinter import ttk

ventana = Tk()
ventana.geometry('600x400')
ventana.title('Grid')
ventana.iconbitmap('C:/Users/rdanchuk/Desktop/Python/Udemy/tkinter/icono.ico')

# Configuramos tamaños de filas y columnas
ventana.rowconfigure(0,weight=1)
ventana.rowconfigure(1,weight=5)
ventana.columnconfigure(0,weight=1)
ventana.columnconfigure(1,weight=5)

# Eventos

def evento1():
    boton1.config(text='Botón 1 presionado',background='red',fg='yellow')
    

def evento2():
    boton2.config(text='Botón 2 presionado')

def evento3():
    boton3.config(text='Botón 3 presionado')

def evento4():
    boton4.config(text='Botón 4 presionado')

# Definimos botones

boton1 = Button(ventana,text='Botón 1',command=evento1)
boton1.grid(row=0,column=0,sticky='NSWE')

boton2 = Button(ventana,text='Botón 2',command=evento2)
boton2.grid(row=1,column=0,sticky='NSWE')

boton3 = Button(ventana,text='Botón 3',command=evento3)
boton3.grid(row=0,column=1,sticky='NSWE')

boton4 = Button(ventana,text='Botón 4', command=evento4)
boton4.grid(row=1,column=1,sticky='NSWE')


ventana.mainloop()