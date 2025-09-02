# Escreva um programa que solicite ao usuário frases. 
# Para parar de solicitar frases, ele pode apenas apertar o “enter”.
# Seu programa deve apresentar cada frase e quantas vezes ela foi repetida.

frases = {}

while True:
  frase = input("Entre com a frase: ")
  if frase == "":
    break

  if frase not in frases:
    frases[frase] = 1

  else:
    frases [frase] += 1

for i, j in frases.items():
  print(i, "->", j)

# %%

