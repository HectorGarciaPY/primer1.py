#Hace una lista con los numeros entre los dos digitos
def fizzList(x,y):
	a=list()
	for i in range(x+1,y):
		a.append(i)
	return a

#Elimina el 3,5 y 7 elemento de una lista
def elim(lista):
	import random
	lista.pop(2)
	lista.pop(3)
	lista.pop(4)
	return lista
	