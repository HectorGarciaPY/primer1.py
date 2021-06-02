while True:
	print("Escribe una secuencia de ADN:")
	x=input()
	print("Cantidad de A: ", x.count("a") + x.count("A"))
	print("Cantidad de C: ", x.count("c") + x.count("C"))
	print("Cantidad de G: ", x.count("g") + x.count("G"))
	print("Cantidad de T: ", x.count("t") + x.count("T"))
	print("Quieres volver a jugar? si o no")
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