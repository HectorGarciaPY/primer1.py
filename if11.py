import calendar
d=int(input("Dime un dia:"))
m = int(input("Dime un mes:(numero)"))
a=int(input("Dime un año:"))
h=int(input("Dime una hora:"))
mi = int(input("Dime los minutos:"))
seg=int(input("Dime los segundos:"))

if a >=0 :
  if m == 1 or m==3 or m == 5 or m==7 or m == 8 or m==10 or m == 12:
    if d>=1 and d<=31:
      print("Es correcta!")
    else:
      print("Es incorrecta...")
  elif m== 4 or m == 6 or m==9 or m == 11:
    if d>=1 and d<=30:
      print("Es correcta!")
    else:
      print("Es incorrecta...")
  elif m== 2:
    if calendar.isleap(a):
      if d>=1 and d<=29:
        print("Es correcta!")
      else:
        print("Es incorrecta...")  
    elif not calendar.isleap(a):
      if d>=1 and d<=28:
        print("Es correcta!")
      else:
        print("Es incorrecta...")
  else:
    print("Es incorrecta...")
else:
  print("Es incorrecta...")
if seg+1== 60:
  print("Si le sumo un segundo a la hora que me has dicho seran las:", h ,":", mi+1,":", 0,".")
  if mi+1==60:
   print("Si le sumo un segundo a la hora que me has dicho seran las:", h+1 ,":", 0,":", seg,".")
   if h+1==24:
    print("Si le sumo un segundo a la hora que me has dicho seran las:", 0 ,":", mi,":", seg,".")

if mi+1==60:
  h+1
if h >=0 and h<=24:
  if mi>=0 and mi<=59:
    if seg>=0 and seg<=59:
      print("Si le sumo un segundo a la hora que me has dicho seran las:", h ,":", mi,":", x,".")
