total=0
i=1
desa=0
aprob=0
for i in range(10):
    nota=int(input("Ingrese nota: "))
    if nota>10:
        aprob=aprob+1
    else:
        desa=desa+1
print("Los aprobados: ",aprob)
print("Los desaprobados: ",desa)