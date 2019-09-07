#Por teclado se ingresa el valor hora de un empleado.Posteriormente se ingresa el nombre del empleado, la antiguedad y la cantidad de horas trabajadas en el mes. Se pide calcular el importe a cobrar teniendo en cuenta que al total que resuelta de multiplicar el valor hora por la cantidad de horas trabajadas, hay que sumarle la cantidad de años trabajados multiplicados por $30, y al total de todas esas operaciones restarle el 13% en concepto de descuentos. Imprimir el recibo correspondiente con el nombre, la antiguedad, el valor hora, el total a cobrar en bruto, el total de descuentos y el valor neto a cobrar.

nombre=str(input("Ingrese el nombre del empleado: "))
valor=int(input("Ingrese el valor por hora: "))
antiguedad=int(input("Ingrese la antiguedad el empleado: "))
cantidad=int(input("Ingrese la cantidad de horas trabajadas al mes: "))

cobrar=(valor*cantidad+antiguedad*30)
descuento=(cobrar/0.13)
final=cobrar-descuento
print("Nombre: ",nombre)
print("Su antiguedad: ",antiguedad)
print("El valor por hora es: ",valor)
print("El total a cobrar es: ",cobrar)
print("El descuento aplicado es de: ",descuento)
print("El dinero a retirar es de : ",final)