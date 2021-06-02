
listaDeLineas=list()

fichero=open("a1.txt","r")
b=fichero.read()
print(b)


def Media():
	for estudiante in listaDeLineas:
		var=0
		for nota in estudiante[1:len(estudiante)-1]:
			var=var+nota
		print("estudiante "+estudiante[0])
		media=var/4
		print(media)
		print(var/len(estudiante[1:]))


		
		
def lecturaArchivos(file):
	fichero=open(file,"r")
	for fila in fichero:	
			listaDeLineas.append(fila)
				

lecturaArchivos("a1.txt")

print(listaDeLineas)

Media()

