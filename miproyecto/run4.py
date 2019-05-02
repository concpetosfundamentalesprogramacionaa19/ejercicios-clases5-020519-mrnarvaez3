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
#  Ingreso de datos
modalidad = input("Ingrese su modalidad\n1.-Distancia \n2.-Presencial \n")

modalidad = int(modalidad)

edad =  input("Ingrese su edad: ")

edad = int(edad)


#  Calcular precio por modalidad
if (modalidad == 1):
	precio = 1200 * 10
else:
	precio = 1200 * 8

#  Calcular precio del seguro
if (edad <= 20) and (modalidad == 1):
	seguro = 100 * 10
else:
	if(edad >20) and (modalidad == 1):
		seguro = 150 * 10

if (edad <= 20) and (modalidad == 2):
	seguro = 100 * 8
else:
	if(edad >20) and (modalidad == 2):
		seguro = 150*8

#  Calcular precio final a pagar
preciofinal = int((precio + seguro))
#  Salida de datos
print("El precio a final a pagar es de: %d$" % preciofinal)		

