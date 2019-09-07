#INGRESAR X CANTIDAD DE PESOS DE UNA PERSONA Y MOSTRAR LA CANTIDAD PERSONAS QUE PESAN MAS DE 80 Y MENOS DE 80 Y APARTE EL PROMEDIO DE PESO DE TODAS LAS PERSONAS
total=0
kg=0
gk=0
cant=int(input("Ingrese la cantidad: "))
for a in range(cant) :
    peso=(int(input("Ingrese el peso: "))
    total=(total+peso)

    if  peso>80 :
        kg=kg+1

    else:
        gk=gk+1

resultado=(total)/cant
print("============================================")
print("Se ha registrado un total de ",kg,"persoanas que pesan mas de 80kg")
print("Se ha registrado un total de ",kg1,"personas que pesan menos de 80 kg")
print("El promedio total el de: ",resultado)

    