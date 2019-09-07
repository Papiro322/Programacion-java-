print(":::::::::::::::::::::::::::::::::")
print("Confirmacion de acceso de Usuario")
print(":::::::::::::::::::::::::::::::::")
import getpass
usu="felipe"
pas="73979202"
usuario=input("Ingrese su Usuario: ")
clave=getpass.getpass("Ingrese se clave: ")
if usu==usuario and pas==clave :
    print("Usuario y contraseña correctas")
    print("Bienvenido: ",usu)
    n1=int(input("Ingrese la nota 1: "))
    n2=int(input("Ingrese la nota 2: "))
    n3=int(input("Ingrese la nota 3: "))
    n4=int(input("Ingrese la nota 4: "))
    print("=============================")
    print(":::::::::::::::::::::::::::::")
    print("=============================")
    prom=(n1+n2+n3+n4)/4
    print("El promedio de las notas ingresadas es: ",prom)

    if prom>10 :
        print("Su nota es: ",prom)
        print("APROBADO")
    else :
        prom<10
        print("Su nota es: ",prom)
        print("Desaprobado")
else:
    print("Usuario y contraseña incorrectas")
    print("Vuelva a intentarlo")
    print("=================================")
 