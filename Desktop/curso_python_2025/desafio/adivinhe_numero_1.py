import random

def get_intervalo():
  while True:
    try:
      numero_min = int(input("Entre com um valor mínimo: "))
      numero_max = int(input("Entre com um valor maximo: "))

    except ValueError as err:
      print("Número inválido - Entre com um valor inteiro válido!", err)
      continue

    if numero_min >= numero_max:
      print("Valor minimo precisa ser menor e diferente que o valor máximo!")
      continue

    return numero_min, numero_max

def get_guess(valor_min, valor_max):
  while True:
    try:
      guess = int(input(f"Entre com um palpite que esteja entre os números {valor_min} e {valor_max}: "))
    
    except ValueError as err:
      print("Valor inválido - Entre com um número inteiro!")
      continue

    if not (valor_min <= guess <= valor_max):
      print("Valor invalido - Entre com um valor que esteja dentro do intervalo!")
      continue

    return guess
  
def main():
  numero_min, numero_max = get_intervalo()
  numero_sorteio = random.randint(numero_min,numero_max)

  for i in range(1,6):
    numero_usuario = get_guess(numero_min, numero_max)

    if numero_usuario == numero_sorteio:
      print(f"Parabéns, voçê acertou na {i}º tentativa!!")
      break

    elif numero_usuario > numero_sorteio:
      print("Número muito alto, tente um número mais baixo!")

    else:
      print("Número muito baixo, tente um número mais alto!")
  
  else:
    print("Que pena, suas tentativas acabaram. O número correto era:", numero_sorteio)

if __name__ == "__main__":            
    main()  