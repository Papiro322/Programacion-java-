import getpass
usu="Juan"
pas="1234"
usuario=input("Ingrese su usuario: ")
clave=getpass.getpass("ingrese clave: ")
if usu==usuario and pas==clave :
    print("Usuario y contraseña correcto")
else:
    print("Usuario y contraseña incorrectas")