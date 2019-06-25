from random import choice

 
print ("Hola, vamos a jugar a piedra, papel o tijera. Elige: \n 1 = Piedra, 2 = Papel, 3 = Tijera " )

Opciones = ['1', '2', '3']
Maquina = choice((Opciones))
Player = input( "-->: ")

if Player == Maquina:
   print("Empate")

if (Player == '1'):
  if (Maquina == '2'):
    print("Perdiste")
  elif (Maquina == '3'):
     print("ganaste")

if (Player == '2'):
  if (Maquina == '3'):
     print("Perdiste")
  elif (Maquina == '1'):
      print("Ganaste")

if (Player == '3'):
  if (Maquina == '1'):
    print("perdiste")
  elif (Maquina == '2'):
    print("ganaste")