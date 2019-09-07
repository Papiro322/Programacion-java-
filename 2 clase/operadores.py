n1=int(input("Ingrese la primera nota: "))
n2=int(input("Ingrese la segunda nota: "))
prom=(n1+n2)/2
if prom>10 :
    print("Su nota es: ",prom)
    print("APROBADO")
else :
    prom<10
    print("Su nota es: ",prom)
    print("Desaprobado")

