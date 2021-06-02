
lista_alumnos=list()
ñ=2

for i in range(ñ):
	nombre=input("Introduce nombre:")
	apellido=input("Introduce apellido:")
	edad=input("Introduce edad:")
	altura=input("Introduce altura:")
	peso=input("Introduce peso:")
	lista_alumnos.append([nombre,apellido,edad,altura,peso])

print("Escoge uno de los participantes:")
for l in range(ñ):
	print("-",lista_alumnos[ñ-l-1][0])
eleccion=input()
if eleccion==lista_alumnos[ñ-l-1][0]:
	
