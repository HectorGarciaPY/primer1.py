def binarizar(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario
while True:		
	x = int(input('Escribe un número para convertirlo a binario: '))
	print(binarizar(x))
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