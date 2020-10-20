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
if seg<= 59 and seg>=0:
  if mi<=59 and mi>=0:
    if h<=23 and h>=0:
      if seg== 59:
        if mi==59:
          if h==23:
            if a>=0:
              if m == 1 or m==3 or m == 5 or m==7 or m == 8 or m==10:
                if d==31:
                  print("Si le sumo un segundo a la hora que me has dicho sera:",1 ,"/",m+1 ,"/", a,"Hora:", 0,":",0,":",0 )
                else:
                  print("Si le sumo un segundo a la hora que me has dicho sera:",d+1 ,"/",m ,"/", a,"Hora:", 0,":",0,":",0 )
              elif m== 4 or m == 6 or m==9 or m == 11:
                if d==30:
                  print("Si le sumo un segundo a la hora que me has dicho sera:",1 ,"/",m+1 ,"/", a,"Hora:", 0,":",0,":",0 )
                else:
                  print("Si le sumo un segundo a la hora que me has dicho sera:",d+1 ,"/",m ,"/", a,"Hora:", 0,":",0,":",0 )
              elif m== 2:
                if calendar.isleap(a):
                  if d==29:
                    print("Si le sumo un segundo a la hora que me has dicho sera:",1 ,"/",m+1 ,"/", a,"Hora:", 0,":",0,":",0 )
                  else:
                    print("Si le sumo un segundo a la hora que me has dicho sera:",d+1 ,"/",m ,"/", a,"Hora:", 0,":",0,":",0 )
                elif not calendar.isleap(a):
                  if d==28:
                    print("Si le sumo un segundo a la hora que me has dicho sera:",1 ,"/",m+1 ,"/", a,"Hora:", 0,":",0,":",0 )
              elif m==12:
                if d==31:
                  print("Si le sumo un segundo a la hora que me has dicho sera:",1 ,"/",1 ,"/", a+1,"Hora:", 0,":",0,":",0 )
                else:
                  print("Si le sumo un segundo a la hora que me has dicho sera:",d+1 ,"/",m ,"/", a,"Hora:", 0,":",0,":",0 )
          else:
            print("Si le sumo un segundo a la hora que me has dicho sera:",d ,"/",m ,"/", a,"Hora:", h+1,":",0,":",0 )
        else:
          print("Si le sumo un segundo a la hora que me has dicho sera:",d ,"/",m ,"/", a,"Hora:", h,":",mi+1,":",0 )             
      else:
          print("Si le sumo un segundo a la hora que me has dicho sera:",d ,"/",m ,"/", a,"Hora:", h,":",mi,":",seg+1 )
    else:
      print("La hora introducida no es correcta.")
  else:
    print("La hora introducida no es correcta.")    
else:
  print("La hora introducida no es correcta.")