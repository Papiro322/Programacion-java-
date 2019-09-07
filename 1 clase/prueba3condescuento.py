print("PROGRAMAS DE CALCULO DE SALARIO MENSUAL")
print("=======================================")
print("BIENVENDO")
print("=======================================")
nombre=str(input("ingrese nombre del trabajador: "))
H=int(input("Ingrese la cantidad de horas trabajadas: "))
C=float(input("Ingrese el costo por hora: "))
pago=(H*C)
print("El monto acumulado es : ",pago)
seguro=pago*0.12
AFP=pago*0.08
descuento=seguro+AFP
totals=pago-descuento
print("Su sueldo sin descuento es:",pago)
print("=======================================")
print("Su descuento de AFP 8%: ",AFP)
print("=======================================")
print("Su descuento de seguro 12%: ",seguro)
perdio=AFP+seguro
print("Se le ha descontado un total de: ",perdio)
print("=======================================")
print("Su pago es: ",totals)
print("=======================================")
print("       GRACIAS POR SU PREFERENCIA: ",nombre)