from tkinter import *

def fun1():
    print('David Casa')

def fun2():
    print('Fernanda Cordova')

def fun3():
    print('Ivonne Vega')

def fun4():
    print('Geovanny Dias')

def botones():
    
    btn1 = Button(ventana, text="Nombre Estudiante 1", command = fun1)
    btn1.pack()

    btn2 = Button(ventana, text="Nombre Estudiante 2", command = fun2)
    btn2.pack()

    btn3 = Button(ventana, text="Nombre Estudiante 3", command = fun3)
    btn3.pack()

    btn4 = Button(ventana, text="Nombre Estudiante 4", command = fun4)
    btn4.pack()

    btn.config(state=DISABLED)

ventana = Tk()
ventana.title('Deber Botones')
btn = Button(ventana, text = "Click Nombre Estudintes", command = botones)
btn.pack()





"""
boton1=Button(ventana,text="David Casa",command=fun1)
boton1.grid(row=1,column=1)
boton2=Button(ventana,text="Fernanda Cordova",command=fun2)
boton2.grid(row=1,column=2)
boton3=Button(ventana,text="Ivonne Vega",command=fun3)
boton3.grid(row=2,column=1)
boton4=Button(ventana,text="Nombre4",command=fun4)
boton4.grid(row=2,column=2)
"""





