def fun1():
    print('David Casa')

def fun2():
    print('Fernanda Cordova')


from tkinter import *
ventana = Tk()
ventana.title('Deber Botones')
boton1=Button(ventana,text="David Casa",command=fun1, bg='red')
boton1.grid(row=1,column=1)
boton2=Botton(ventana,text="Fernanda Cordova",command=fun2)
boton2.grid(row=1,column=2)

