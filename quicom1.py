print("Escoge cara o cruz")
x=input()
import random
y=random.randint(0,1)
if y==1:
  print("Ha salido: Cara")
elif y==0:
  print("Ha salido: Cruz")
if y==1 and x=="cara" or y==0 and x=="cruz":
  print("Has ganado!!!")
else:
  print("Has perdido...")
 

