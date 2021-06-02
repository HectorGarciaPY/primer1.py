import random
a=random.randint(0,9)
while True:
	b=int(input("Dime un numero del 0 al 9:\n"))
	if a==b:
		print("LO HAS ACERTADO!")
		break 
	elif b>9 or b<0: 
		print("Vuelve a intentarlo")		
	print("¿Quieres seguir jugando?")
	print("¿si o no?")
	h=input()
	if h=="si":
		print("Perfecto")
		print("----------")
	elif h=="no":
		print("Hasta la proxima.")
		break
	else:
		print("No te he entendido.")
		print("¿Quieres seguir jugando?")
		print("¿si o no?")
		o=input()
		if o=="si":
			print("Perfecto")
			print("----------")
		elif o=="no":
			print("Hasta la proxima.")
			break
		else:
			print("No te he entendido.")	