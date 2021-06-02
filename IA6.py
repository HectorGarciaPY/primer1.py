recetas=list()
ñ=2
for i in range(ñ):
	nombre=input("Introduce nombre:")
	ingrediente=input("Introduce ingrediente principal:")
	calorias=input("Introduce calorias:")
	dificultad=input("Introduce dificultad:")
	explicacion=input("Introduce explicacion:")
	print(" ")
	recetas.append([nombre,ingrediente,calorias,dificultad,explicacion])
for receta in recetas:
	for i in receta:
		print(i)
eli=int(input("Que receta quieres eliminar?(1 al 2)"))
if eli==1:
	recetas.pop(0)
elif eli==2:
	recetas.pop (1)
for receta in recetas:
	for i in receta:
		print(i)
actre=int(input("De que receta quieres actuaizar un elemento?"))
actel=int(input("Que elemento de la receta quieres eliminar?(1 al 5):"))
if actre==1:
	nuevo=input("Escribe lo nuevo:")
	recetas[0][actel-1]=nuevo
elif actre==2:
	recetas[1][actel-1]=input("Escribe lo nuevo:")
for receta in recetas:
	for i in receta:
		print(i)	

	