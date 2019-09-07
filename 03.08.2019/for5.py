#DESARROLLAR UN PROGRAMA QUE SOLICITE LA CARGA DE 10 NUMEROS Y ME SUME SOLO LOS 5 ULTIMOS NUMEROS

A=1
total=0
for A in range(10) :
    valor=int(input("Ingrese un valor: "))

    if A>4:
        total=total+valor
print("La suma es: ",total)
