# Escreva um programa que solicite ao usuário um nome e uma idade, 
# e crie um dicionário com essas informações. 
# Em seguida, exiba o dicionário.

# %%
nome = input("Qual o seu nome: ")
idade = int(input("Qual a sua idade: "))
# %%
informacao = {"nome": nome, "idade": idade}

type(nome)

# print(type(informacao))
print(informacao)
# %%
