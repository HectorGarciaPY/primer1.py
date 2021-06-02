listaDeLineas=list()
fichero=open("a1.txt","r")
b=fichero.read()
print(b)

def Media():
	a=0
	b=open("a1.txt","r")
	for fila in b:	
		for i in fila:
			a=a+int(fila[i+1:-1])

Media()
print (listaDeLineas)











#def ContarPalabras():
#	contar=len(b.split())
#	print(contar)


#def se_repite(lista):
#	frecuencia = []
#	for w in lista:
#		frecuencia.append(lista.count(w))
#		print(frecuencia)
#	a = frecuencia.index(max(frecuencia))
#	print("la palabra que mas se repite es: " , lista[a])
#ContarPalabras()
#se_repite(b.split())
#
#def MostrarDatos():	