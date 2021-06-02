while True:
	print("Escribe Una frase toda en minusculas:")
	x=input()
	print(x.title())
	print("Numero de palabras: ", x.count(" ")+1)
	print("Numero de caracteres: ", x[(len)]-x.count(" "))
	print("")
	print("Quieres volver a jugar?")
	z=input()
	if z=="si":
		print("")
		continue
	elif z=="no":
		print("Vale, hasta la proxima.")
		break
	else:
		print("No te he entendido, hasta la proxima.")
		break		