#crea un programa de
import getpass
usu="luisitomagoxd"
pas="sebas-tian"
USUARIO= input("ingrese Usuario: ")
CONTRASENA=getpass.getpass("ingrese contraseña: ")
print("======================================")
print("PROGRAMA DE ")
print("======================================")  
print("Menu de Opciones")
print("1. mostrar")
print("2. ocultar")
print("3. eliminar")
print("4. recuperar")

import getpass
mostrar="1"
ocultar="2"
eliminar="3"
recuperar="4"
USUARIO= input("Indique la Opcion del Menu[1,2,3,4]:")
if mostrar==USUARIO:
    print("la operacion es mostrar")
    print("===============================")
    n1=str(input("Ingrese el nombre de la carpeta: "))

    print("Se ha mostrado correctamente la carpeta: ",n1)
else:
    if ocultar==USUARIO:
        print("la operacion es ocultar")
        print("===============================")
        n1=str(input("Ingrese el nombre de la carpeta: "))
        print("Se ha ocultado correctamente la carpeta : ",n1)
    else:
        if eliminar==USUARIO:
            print("la operacion es eliminar")
            print("===============================")
            n1=str(input("Ingrese el nombre de la carpeta: "))
            print("Se ha eliminado correctamente la carpeta : ",n1)
        else:
            if recuperar==USUARIO:
                print("la operacion es recuperar")
                print("===============================")
                n1=(input("Ingrese el nombre de la carpeta: "))
                print("Se ha recuperado correctamente la carpeta : ",n1)
            else:
                print("Error Opcion incorrecto", USUARIO )
            