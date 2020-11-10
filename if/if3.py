print("Pon un numero:")
x=int(input())
print("Pon otro:")
y=int(input())
print("Uno mas porfavor:")
z=int(input())
if x<y<z:
  print(x, y, z)
if y<x<z:
  print(y, x, z)
if z<y<x:
  print(z, y, x)
