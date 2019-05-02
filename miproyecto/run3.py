""" 
	file: run3.py
	autor: @Robert

	nota a mayor o igual a 18: sobresaliente

	nota mayor o igual a 16 y menos a 18: muy buena

	nota mayor o igual a 13 y menor a 6: buena

	nota menor a 13: insuficiente
"""

from misvariables import*

#  uso condicional simple



nota = input("Ingrese su nota 1: ")


nota = int(nota)

if (nota >= 18):
	print("sobresaliente, - nota %d" % nota)
else:
	if (nota >= 16) and (nota < 18):
		print("muy buena, - nota %d" % nota)
	else:
		if (nota >= 13) and (nota < 16):
			print("buena, - nota %d" % nota)
		else:
	 		print("insuficiente, - nota %d" % nota)	




"""
if nota >= 18:
	print("%s, su valor de nota es %d" % (mensaje, nota))
else:
	print("%s, su valor de nota es %d" % (mensaje2, nota))

if nota2 >= 18:
	print("%s, su valor de nota es %d" % (mensaje, nota2))
else: 
	print("%s, su valor de nota es %d" % (mensaje2, nota2))	
"""