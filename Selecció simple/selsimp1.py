print("Selecciona un coche:")
print("a) Porsche")
print("b) Lamborghini")
print("c) Maserati")
x=input()
if x=="a" or x=="A" or x=="a)" or x=="Porsche" or x=="porsche" or x=="Porche" or x=="porche" or x=="Porxe" or x=="porxe":
  print("Has escogido un Porsche")  
elif x=="b" or x=="B" or x=="b)" or x=="Lamborghini" or x=="lamborghini" or x=="Lamborgini" or x=="lamborgini" or x=="Lambo" or x=="lambo":
  print("Te van los Lamborghinis") 
elif x=="c" or x=="C" or x=="c)" or x=="Maserati" or x=="maserati" or x=="Maseratti" or x=="maseratti" or x=="Maseraty" or x=="maseratty":
  print("Has escogido un Maserati")
else:
  print("Vuelve a intentarlo que no te entiendo")