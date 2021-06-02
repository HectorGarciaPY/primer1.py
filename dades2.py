listaDeLineas=list()

def GanadorSegunMariano():
	ganador=["",0]
	for corredor in listaDeLineas:
		puntos=0
		for posicion in corredor:
			if posicion==1:
				puntos=puntos+20
			if posicion==2:
				puntos=puntos+10
			if posicion==3:
				puntos=puntos+5
		if puntos>ganador[1]:
			ganador[0]=corredor[0]
			ganador[1]=puntos
		#Si corredor.puntos>ganador.puntos--> ganador.nombre=corredor.nombre
	for x in ganador:
		print (x)


def GanadorSegunHector():
	for corredor in listaDeLineas:
		var=0
		for posicion in corredor[1:]:
			var=var+posicion
		print("corredor "+corredor[0])
		media=var/3
		print(media)
		print(var/len(corredor[1:]))

def Existe(nombreCorredor,posicion):
	for fila in listaDeLineas:
		if fila[0]==nombreCorredor:
			fila.append(posicion)
			return False
	return True
		
		
def lecturaArchivos(file):
	fichero=open(file,"r")
	for fila in fichero:	
		for i in range(len(fila)):
			if fila[i]==" " and Existe(fila[0:i],int(fila[i+1:-1])):
				listaDeLineas.append([fila[0:i],int(fila[i+1:-1])])
				
for j in [1,2,3]:
	lecturaArchivos("a"+str(j)+".txt")

print(listaDeLineas)

GanadorSegunHector()
GanadorSegunMariano()
