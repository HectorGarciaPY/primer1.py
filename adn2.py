while True:
	print("Escribe una secuencia de ADN:")
	x=input()
	print("Cantidad de purinas: ", x.count("ag") + x.count("AG") + x.count("aG") + x.count("Ag"))
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