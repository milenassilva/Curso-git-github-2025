# Peça ao usuário para informar um intervalo mínimo e máximo (exemplo: 10 a 50).
# Sorteie um número dentro desse intervalo.
# O usuário terá 5 tentativas para adivinhar.
# Após cada tentativa, o programa deve dizer se o número sorteado é maior ou menor.
# Se o usuário acertar, mostre "Parabéns, você acertou!" e encerre o jogo.
# Caso ele não acerte em 5 tentativas, mostre "Você perdeu! O número era X".

import random

numero_min = int(input("Entre com um número minimo: "))
numero_max = int(input("Entre com um número máximo: "))

numero_sorteio = random.randint(numero_min, numero_max)

for i in range(5):
  numero_usuario = int(input("Agora entre com o número para ser sorteado: "))
  
  if numero_sorteio == numero_usuario:
     print("Parabéns, você acertou!")
     break
  
  elif numero_usuario > numero_sorteio:
     print("Número muito alto. Tente um número menor!")

  else:
     print("Número muito baixo. Tente um número maior!")
  
else: 
   print("Você perdeu! O número era:", numero_sorteio)

    
