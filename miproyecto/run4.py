"""
	file "run4.py"
	autor "@Robert0"
deaeamos obtener el costo de una carrera universitaria. El valor
promedio de cada ciclo es de 1200$.
El valor promedio del seguro 
educativo por ciclo es de 100$ si la edad del estudiante es <=20.
Caso contrario sera de 150$
Si el estudiante tiene una modalidad a distancia el numero de ciclos a seguir es de 10.
De lo contrario debera seguir 8 ciclos.
obtener el costo final de la carrera para un estudiante
"""

modalidad = input("Ingrese su modalidad\n1.-Distancia \n2.-Presencial \n")

modalidad = int(modalidad)

edad =  input("Ingrese su edad: ")

edad = int(edad)


precio = int(precio)
seguro = int(seguro)


if modalidad == 1:
	precio = 1200 * 10
else:
	precio = 1200 * 8

if edad <= 20 and modadlidad ==1:
	seguro = 100 * 10
if edad >20 and modalidad == 2:
 	seguro = 150 * 8

preciofinal = float(costo + seguro)

print("El precio a final a pagar es de: %.2f" % preciofinal)		

