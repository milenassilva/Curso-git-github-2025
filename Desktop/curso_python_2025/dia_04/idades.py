# %%

idades = [] # Criamos a lista vazia para armazenar dados nela

while True: # Criamos o laço pedindo o input para o usuário ir colocando os numeros
  idade = input("Entre com a idade: ")

  if idade == "": # Criamos uma condição: se o usuário não colocar a idade, interrompe o laço e se for colocando as idades, vai armazenando e adicionando na lista, que é o codigo de baixo 'append'
    break

  idades.append(int(idade))

print(idades)

media = sum(idades) / len(idades) # sum() é a soma da variavel idades e o len() é quantidade de idades que foi colocado
minimo = min(idades)
maximo = max(idades)
qtde = len(idades)

print("MEDIA:", media)
print("MINIMO:", minimo)
print("MAXIMO:", maximo)
print("QTDE:", qtde)