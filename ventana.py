from tkinter import*
ventana= Tk()
ventana.title("Sistema de ventas")
colorfondo="#00acee"
ventana.configure(background=colorfondo)
ventana.geometry("400x200")
etiqueta1 = Label(ventana, text="Contro de Asistencia").place(x=150,y=10)
etiqueta2 = Label(ventana, text="Usuario").place(x=90,y=40)
etiqueta3 = Label(ventana, text="Password").place(x=90,y=70)
cuadro1=Entry(ventana,text="Ingrese su Usuario..").place(x=180,y=40)
cuadro2=Entry(ventana,text="Ingrese su Password..").place(x=180,y=70)
boton1=Button(ventana,text="Ingresar",width=12,height=2 ).place(x=90,y=100)
boton1=Button(ventana,text="Salir",width=12,height=2,command=ventana.quit).place(x=210,y=100) 


ventana.mainloop()
