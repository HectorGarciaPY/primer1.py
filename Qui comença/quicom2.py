import random
print("Com et dius?")
nom=input()
print("Que vols?")
print("a) Parells")
print("b) Senars")
x=input()
if x=="a" or x=="b":
	print("Posa el nombre de dits extesos:")
	y=int(input())
	z=random.randint(0,10)
	j=y+z
	if y<11 and y>-1:
		if x=="a":
			if j%2==0:
				print("Has guanyat", nom, "la suma ha sortit", y+z,"perque l'ordinador ha tret", z)
			else:
				print("Has perdido", nom, "Perque la suma ha sortit",y+z) 
		elif x=="b":
			if j%2==1:
				print("Has guanyat", nom, "la suma ha sortit", y+z,"perque l'ordinador ha tret", z)
			else:
				print("Has perdido", nom, "Perque la suma ha sortit",y+z)
	else:
		print("Prueba otra vez.")
else:
  print("Prueba otra vez.") 
  
