import random
a=random.randint(0,9)
while True:
	b=int(input("Dime un numero del 0 al 9:\n"))
	if a==b:
		print("LO HAS ACERTADO!") 
		break
	elif b>9 or b<0: 
		print("Vuelve a intentarlo")
		break		