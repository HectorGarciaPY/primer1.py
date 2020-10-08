print("Dime el precio que has pagado por el producto")
x=int(input())
print("Dime el precio del producto sin descuento")
y=int(input())
c=y-x
a=x*100/y
b=round(100-a)
if c>0:
  print("Te has ahorrado:", c, "€.")
if c<0:
  print("Lo siento chavalin,")
if b>0:
  print("Te han hecho un descuento del:", b, "%." )
if b<0:
  print("no te has ahorrado nada.F")