import math 
a=int(input("Dime el primer numero:"))
b=int(input("Dime el segundo numero:"))
c=int(input("Dime el tercer numero:"))
print("El resultado positivo:", (-b+math.sqrt(b**2-(4*a*c)))/(2*a) )
print("El resultado negativo:", (-b-math.sqrt(b**2-(4*a*c)))/(2*a) )
