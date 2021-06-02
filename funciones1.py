import math
def area_circulo(radio):
	return math.pi * radio * radio

radio=int(input("Escriba el radio de la circumferencia: "))
print("El area de la circumferncia es: ",round(area_circulo(radio)))