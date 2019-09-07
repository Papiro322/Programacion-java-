#INGRESAR EN LA PANTALLA N NUMEROS
    valor=int(input("Ingrese la cantidad de veces a repetir: "))

    valores=[]

#EL PROGRAMA PEDIRA UN VALOR LA CANTIDAD DE VECES DE N
n=1
total=0
for n in range(valor) :
    valores=int(input("Ingrese un valor: "))
    total=total+valores

print("========================================")
print("La suma de todos los valores es: ",total)