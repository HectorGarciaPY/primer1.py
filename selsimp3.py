print("Dime una cara del dado y te dire la cara opuesta:")
x=int(input("Cara:"))
if x>0 and x<7:
  print("La cara opuesta es:", 7-x)
else:
  print("Vuelve a intentarlo.")  