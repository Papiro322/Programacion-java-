def pantalla():
    print("______________________________________")
    print("_______________BIENVENIDO_____________")
    print("______________________________________")
    print("1.-CAMBIO DE SOLES A DOLARES: " )
    print("2.-CAMBIO DE DOLARES A SOLES: " )
    print("3.-CAMBIO DE SOLES A EUROS: ")
    print("______________________________________")

def proceso(opcion):
    if opcion==1:
       print("calcula Soles") 

    elif opcion==2:
       print("calcula dolares")
    elif opcion==2:
       print("calcula dolares")

def ingreso():
    a=int(input("ingrese opcion:"))
    proceso(a)

pantalla()
ingreso()
