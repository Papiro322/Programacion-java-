def cantidad_vocales(cadena):
    cant=0
    for x in range(len(cadena)):
        if cadena[x]=="a" or cadena[x]=="e" or cadena[x]=="i" or cadena[x]=="o" or cadena[x]=="u":
            cant=cant+1
    print("Cantidad de vocales de palabra",cadena,"es",cant)

#BLOQUE PRINCIPAL
cantidad_vocales("Hola")
cantidad_vocales("administracion")
cantidad_vocales("correr") 
#ACTIVIDADES:      
#BUSCAR 50 FUNCIONES DE PAYTON Y PONER CUAL ES SU FUNCION
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::