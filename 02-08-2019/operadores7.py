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
    curso1="matematica"
    curso2="Fisica"

    curso=input("Ingrese su materia: ")

    if  curso1==curso :
        print("==============================================")
        print("Bienvenido al registro de notas de matematica:")
        print("==============================================")

        n1=int(input("Ingrese Nota 1: "))
        n2=int(input("Ingrese Nota 2: "))
        prom=(n1+n2)/2
        print("Su promedio es : ", prom)
        if prom>10:
            print("Aprobado")
        else :
            print("Desaprobado")     

    else:
        print("Usuario Correcto")
        print("Bienvenido ", usuario )
        print("===============================")
        print("Bienvenido al curso de fisica")
        print("===============================")
        n1=int(input("Ingrese Nota 1: "))
        n2=int(input("Ingrese Nota 2: "))
        n3=int(input("Ingrese Nota 3: "))
        n4=int(input("Ingrese Nota 4: "))
        prom1=(n1+n2+n3+n4)/4
        print("Su promedio es : ", prom1)
        if prom1>10:
            print("Aprobado")
        else:
            print("Desaprobado")  
else :
    usu2==usuario and pas2==clave
    print("Usuario Correcto")
    print("Bienvenido ", usuario )
    print("===============================")
    curso1="matematica"
    curso2="Fisica"

    curso=input("Ingrese su materia: ")
    if  curso1==curso :
        print("==============================================")
        print("Bienvenido al registro de notas de matematica:")
        print("==============================================")

        n1=int(input("Ingrese Nota 1: "))
        n2=int(input("Ingrese Nota 2: "))
        prom=(n1+n2)/2
        print("Su promedio es : ", prom)
        if prom>10:
            print("Aprobado")
        else :
            print("Desaprobado")     

    else:
        print("Usuario Correcto")
        print("Bienvenido ", usuario )
        print("===============================")
        print("Bienvenido al curso de fisica")
        print("===============================")
        n1=int(input("Ingrese Nota 1: "))
        n2=int(input("Ingrese Nota 2: "))
        n3=int(input("Ingrese Nota 3: "))
        n4=int(input("Ingrese Nota 4: "))
        prom1=(n1+n2+n3+n4)/4
        print("Su promedio es : ", prom1)
        if prom1>10:
            print("Aprobado")
        else:
            print("Desaprobado")  

    