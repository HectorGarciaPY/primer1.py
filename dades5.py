listaDeLineas=list()


def lecturaArchivos(file):
	fichero=open(file,"r")
	for fila in fichero:
		posicionComa=0	
		alumno=[]
		for i in range(len(fila)):
			if fila[i]==",":
				alumno.append(fila[posicionComa:i])
				posicionComa=i+2
				crearArchivo(fila[0:i],fila[i+1:-1])	
		alumno.append(fila[posicionComa:-1])
		listaDeLineas.append(alumno)
				


def crearArchivo(NombreArchivo,Asignaturas):
	fichero1=open(NombreArchivo+".txt","w")
	fichero1.write("Hola,\nestás matriculado de las asignaturas: "+Asignaturas)

lecturaArchivos("a2.txt")

print(listaDeLineas)

#fila[i+1:-1]