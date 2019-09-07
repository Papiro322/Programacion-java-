#crear un programa que permita cargar el usuario y contraseña, #Si no es corrrecto 3 veces, votarlo del sistema

print(":::::::::::::::::::::::::::::::::")
print("Confirmacion de acceso de Usuario")
print(":::::::::::::::::::::::::::::::::")
import getpass
usu="juan"
pas="1234"
sesion=-0
(sesion==0)
usuario=input("Ingrese su Usuario: ")
clave=getpass.getpass("Ingrese su clave: ")
usuario==usu
pas==clave
if usu==usuario and pas==clave:
    print("Usuario y contraseña correctas")
    print("Bienvenido: ",usu)
    sesion<-1
else:
    print("Usuario y contraseña incorrectas")
    print("Vuelva a intentarlo")
    print("=================================")