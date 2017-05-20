def fun1():
    print('David Casa')

from tkinter import *
ventana = Tk()
ventana.title('Deber Botones')
boton1=Button(ventana,text="David Casa",command=fun1, bg='red')
boton1.grid(row=1,column=1)

