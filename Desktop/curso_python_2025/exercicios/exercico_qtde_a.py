# %%
palavra = input("Digite uma palavra:") # Input para o usuario entrar com a palvra
contador = 0 # criamos uma caixinha vazia, para a contagem das letras

for letra in palavra: # Para cada 'letra' em palavra
  if letra == "a": # SE a letra for "a"
    contador += 1 # O contador armazena +1, e isso se repete letra por letra da palavra digitada, ate finalizar a palavra inteira

print("A palavra digitada, possui:", contador, "'a'")