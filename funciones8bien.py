def recogida(numL):
	l=[]
	for i in range(2):
		l.append(int(input("Numero de Lista "+str(numL),":")))
	return l

def comparar(a,b):
	for i in a:
		for j in b:	
			if i == j:
				return True
	return False

ListaGeneral = []
NumListas = int (input("¿Cuántas listas quieres comparar?"))

#Recogida de datos
for var in range(NumListas):
	ListaGeneral.append(recogida(var))

#Comparación Listas
for i in range(len(ListaGeneral)):
	for j in range(i+1 , len(ListaGeneral)):
		if comparar(ListaGeneral[i] , ListaGeneral[j]):
			print("Hay coincidencia")
			break
