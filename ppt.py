from random import choice

 
print ("Hola, vamos a jugar a piedra, papel o tijera." )

Opciones = [1, 2, 3]
Maquina = choice(Opciones)
Eleccion = int(input( 1 '= Piedra', 2 '= Papel', 3 '= Tijera '))

if Eleccion == Maquina:
   print("Empate")

if (Eleccion == 1):

  if (Maquina == 2):
    print("Perdiste")
  elif (Maquina == 3):
     print("ganaste")

if (Eleccion == 2):
  if (Maquina == 3):
     print("Perdiste")
  elif (Maquina == 1):
      print("Ganaste")

if (Eleccion == 3):
  if (Maquina == 1):
    print("perdiste")
  elif (Maquina == 2):
    print("ganaste")