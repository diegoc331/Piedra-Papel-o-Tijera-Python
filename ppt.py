from random import choice

inicio = input('Elige 1 para jugar ó 2 para salir --> ')

if inicio == '1':
  
  print ("Hola, vamos a jugar a piedra, papel o tijera. Elige una de las siguientes opciones: \n 1 = Piedra \n 2 = Papel \n 3 = Tijera \n 4 = Salir " )

  Opciones = ['1', '2', '3']
  Maquina = choice((Opciones))
  Player = input( "-->: ")

  if Player == Maquina:
    print("Empate")

  if (Player == '1'):
    if (Maquina == '2'):
      print("Perdiste")
    elif (Maquina == '3'):
      print("Ganaste")

  if (Player == '2'):
    if (Maquina == '3'):
      print("Perdiste")
    elif (Maquina == '1'):
        print("Ganaste")

  if (Player == '3'):
    if (Maquina == '1'):
      print("Perdiste")
    elif (Maquina == '2'):
      print("Ganaste")
else:
  print ('Bye!')