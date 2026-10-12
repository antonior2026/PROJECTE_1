import math

while True:
 print("Benvingut/da a la millor calculadora del món!")
 print("Què vols fer?")
 print("--------------------\n1: Operacions bàsiques\n2: Logaritmes i exponencials\n3: Trigonometria\n4: Conversions\n5: Sortir\n--------------------")
 
 Menú = int(input("Escull: "))
 print("--------------------")

 if (Menú==1):
  print("--------------------\nQuina modalitat esculls?")
  print("1: Sumar\n2: Restar\n3: Multiplicació\n4: Divisió")

  Menu2 = int(input("--------------------\nModalitat: "))
  print("--------------------")

 elif (Menú==2):
  print("Quina modalitat esculls?")
  print("5: Arrels Quadrades\n6: Logaritmes\n7: Factorial")

  Menu2 = int(input("--------------------\nModalitat: "))
  print("--------------------")

 elif (Menú==3):
  print("Quina modalitat esculls?")
  print("8: Cosinus\n9: Sinus\n10: Tangent\n11: Pi\n12: e")

  Menu2 = int(input("--------------------\nModalitat: "))
  print("--------------------")

 elif (Menú==4):
  print("Quina modalitat esculls?")
  print("13: Graus centigrads\n14: Radiants") 
  
  Menu2 = int(input("--------------------\nModalitat: "))
  print("--------------------")

 elif (Menú==5):
    print("Gràcies per utilitzar la millor calculadora!")
    print("--------------------")
    break

 else:
   print("Has d'escollir un número entre l'1 i el 5!")
   print("--------------------")

   continue

 if (Menu2==1):
   sumant1 = float(input("Introdueix el primer sumant: "))
   sumant2 = float(input("Introdueix el segon sumant: "))
   print("Resultat de la suma: ", sumant1 + sumant2)
   print("--------------------")
 
 elif (Menu2==2): 
    restant1 = float(input("Introdueix el primer restant: "))
    restant2 = float(input("Introdueix el segon restant: "))
    print("Resultat de la resta: ", restant1 - restant2)
    print("--------------------")
 
 elif (Menu2==3):
    multiplicant1 = float(input("Introdueix el primer multiplicant: "))
    multiplicant2 = float(input("Introdueix el segon multiplicant: "))
    print("Resultat de la multiplicació: ", multiplicant1 * multiplicant2)
    print("--------------------")
 
 elif (Menu2==4):
    divident1 = float(input("Introdueix el divident: "))
    divisor2 = float(input("Introdueix el divisor: "))
    if (divisor2 == 0):
     print("El resultat és infinit.")  
    if (divisor2 < 0):
     print("Resultat de la divisió: ", divident1 / divisor2)
    if (divisor2 > 0):
     print("Resultat de la divisió: ", divident1 / divisor2)
     print("--------------------")

 elif (Menu2==5):
    arrel1 = float(input("Introdueix un nombre: "))
    if (arrel1 < 0):
     print("No pots fer l'arrel d'un nombre negatiu!")
    if (arrel1 >= 0):
     print("Resultat de l'arrel: ", math.sqrt(arrel1))
     print("--------------------")

 elif (Menu2==6):
    x = float(input("Introdueix la base: "))
    base = float(input("Introdueix l'exponent': "))
    print("Resultat del logaritme: ", (math.log(x)/math.log(base)))
    print("--------------------")

 elif (Menu2==7):
    x = float(input("Introdueix un nombre: "))
    print("Resultat del factorial: ", math.factorial(x))
    print("--------------------")

 elif (Menu2==8):
    cos = float(input("Introdueix un nombre: "))
    print("Resultat del cosinus és: ", math.cos(math.radians(cos)))
    print("--------------------")

 elif (Menu2==9):
    sin = float(input("Introdueix un nombre: "))
    print("Resultat del sinus és: ", math.sin(math.radians(sin)))
    print("--------------------")

 elif (Menu2==10):
    tan = float(input("Introdueix un nombre: "))
    print("Resultat del tangent és: ", math.tan(math.radians(tan)))
    print("--------------------")

 elif (Menu2==11): 
    x = math.pi
    print("Pi: ", x)
    print("--------------------")

 elif (Menu2==12): 
    x = math.e
    print("e: ", x)
    print("--------------------")

 elif (Menu2==13):
    radians = float(input("Introdueix els radians que vols covertir: "))
    x = (radians)
    resultat = math.degrees(x)
    print("Graus: ", resultat)
    print("--------------------")

 elif (Menu2==14):
    graus = float(input("Introdueix els graus centigrads que vols covertir: "))
    x = (graus)
    resultat = math.radians(x)
    print("Radians: ", resultat)
    print("--------------------")

 else:
    print("Ep! Has d'escollir un número entre l'1 i el 15!")
    print("--------------------")