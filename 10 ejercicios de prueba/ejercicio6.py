print("BIENVENIDO AL PROGRAMA DE CALCULO DE AREAS DE TRIANGULOS")
print("=====================================================================")
LongitudA=int(input("Ingrese una longitud del triangulo: "))
LongitudB=int(input("Ingrese una longitud del triangulo: "))
LongitudC=int(input("Ingrese una longitud del triangulo: "))
print("=====================================================================")
LongitudDelSemiperimetro=(LongitudA+LongitudB+LongitudC)/2
print("La longitud del perimetro es: ",LongitudDelSemiperimetro)
AreadelTriangulo=(LongitudDelSemiperimetro*(LongitudDelSemiperimetro-LongitudA)*(LongitudDelSemiperimetro-LongitudB)*(LongitudDelSemiperimetro-LongitudC))**0.5
print("El area del triangulo es: ",AreadelTriangulo)
print("==========================")
print("GRACIAS POR SU PREFERENCIA")
print("==========================")