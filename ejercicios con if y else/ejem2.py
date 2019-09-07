import getpass
usu="luis"
pas="1234"
usu2="felipe"
pas2="1234"
usu3="lion"
pas3="1234"
usuario=input("Ingrese su Usuario: ")
clave=getpass.getpass("Ingrese su Password: ")
if usu==usuario and pas==clave:
    print("Usuario Correcto")
    print("Bienvenido ", usuario )
    print("===============================")
    n1=int(input("Ingrese Nota 1: "))
    n2=int(input("Ingrese Nota 2: "))
    n3=int(input("Ingrese Nota 3: "))
    n4=int(input("Ingrese Nota 4: "))
    prom=(n1+n2+n3+n4)/4
    print("Su promedio es : ", prom)
    if prom>10:
      print("Aprobado")
    else :
      print("Desaprobado")     

else:
    if usu2==usuario and pas2==clave:
        print("Usuario Correcto")
        print("Bienvenido ", usuario )
        print("===============================")
        n1=int(input("Ingrese Nota 1: "))
        n2=int(input("Ingrese Nota 2: "))
        n3=int(input("Ingrese Nota 3: "))
        n4=int(input("Ingrese Nota 4: "))
        prom=(n1+n2+n3+n4)/4
        print("Su promedio es : ", prom)
        if prom>10:
            print("Aprobado")
        else:
            print("Desaprobado")  


    else:    
        if usu3==usuario and pas3==clave:
            print("Usuario Correcto")
            print("Bienvenido ", usuario )
            print("===============================")
            n1=int(input("Ingrese Nota 1: "))
            n2=int(input("Ingrese Nota 2: "))
            n3=int(input("Ingrese Nota 3: "))
            n4=int(input("Ingrese Nota 4: "))
            prom=(n1+n2+n3+n4)/4
            print("Su promedio es : ", prom)
            if prom>10:
                print("Aprobado")
            else :
                print("Desaprobado")  

        else:    
            print("Usuario Incorrecto")
            print("Ud no se ha registrado", usuario )
