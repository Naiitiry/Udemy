from tkinter import *
from tkinter import ttk

########### FUNCIONES ###########

def evento_clic():
    boton1.config(text='Botón presionado.')
    print('Ejecución')


ventana = Tk()
ventana.geometry('500x500')
ventana.title('Nueva ventana')
ventana.iconbitmap('C:/Users/rdanchuk/Desktop/Python/Udemy/tkinter/icono.ico')


boton1 = ttk.Button(ventana,text='Botón',command=evento_clic)
boton1.pack()



ventana.mainloop()