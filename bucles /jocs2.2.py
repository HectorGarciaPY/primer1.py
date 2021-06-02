import random
while True:
	for i in range(6):
		x=random.randint(1,49)
		print(x)
	print("")
	print("¿Te gusta esta combinacion?")
	print("¿si o no?")
	a=input()
	if a=="no" or a=="No" or a=="NO" or a=="nO":
		print("Perfecto, continuemos.")
		print("")
		continue
	elif a=="si" or a=="Si" or a=="SI" or a=="sI":
		print("Vale, hasta la proxima.")
		break
	else:
		print("Vuelve a intentarlo:")
		print("")
				