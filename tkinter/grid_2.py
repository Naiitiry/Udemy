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


boton1 = ttk.Button(ventana,text='Botón 1')
boton1.grid(row=0,column=0,sticky='NSWE')

boton2 = ttk.Button(ventana,text='Botón 2')
boton2.grid(row=1,column=0,sticky='NSWE')

boton3 = ttk.Button(ventana,text='Botón 3')
boton3.grid(row=0,column=1,sticky='NSWE')

boton4 = ttk.Button(ventana,text='Botón 4')
boton4.grid(row=1,column=1,sticky='NSWE')


ventana.mainloop()