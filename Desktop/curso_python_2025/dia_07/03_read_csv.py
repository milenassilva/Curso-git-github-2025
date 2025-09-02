# %%

arquivos = "data.csv"

with open(arquivos) as open_file:
  lines = open_file.readlines() # esse readlines transforma as linha em listas

for l in lines: # Aqui criamos um laço para pecorrer pela lista que criamos la em cima com o readlines. ler assim: para cada l em lines, imprima l
  print(l)

# %%

dados = dict() # aqui criamos um dicionario vazio

chaves = lines[0].strip("\n").split(";") # Aqui estamos definindo quem são as chaves e elas estão na posição zero. esse strip está removendo o \n, o split está fatiando apartir do ';'
for c in chaves: # Aqui criamos um laço para pecorrer pela lista. ler assim: para cada c em chaves, faça:
  dados[c] = [] # aqui estamos definindo que para cada item que chamos de c em dados, vamos criar uma lista vazia

# %%

for l in lines[1:]: # estamos pecorrendo o restante das linhas do arquivo, começamos com a 2° linha até o final

  valores = l.strip("\n").split(";") #para cada uma estamos fazendo o mesmo que fizemos com as chaves

  for i in range(0, len(valores)): # o range é para gerar do zero até o numero certo de valores que tem no arquivo. esta pecorrendo o indice que definimos como i que começa e 0 até o numero de valores que tem no arquivo

    dados[chaves[i]].append(valores[i]) # Aqui estamos garantindo que cada valor na mesma posição das chaves
    # o append é um método que serve para dicionar um item no final da lista

dados
# %%

idades = [] # Criando uma lista vazia
for i in dados["idade"]: # pecorrendo um laço na posição idade
  idades.append(int(i)) # aqui estamos adiciando na lista que criamos vazia e transformando ela em inteiro

media = sum(idades)/ len(idades)

media
# %%
