# %%
nome_arquivo = "historia.txt"

with open(nome_arquivo) as open_file:
  conteudo = open_file.read() 
# essas duas linhas já faz o papel de todo o codigo abaixo que está comentado, faz exatamente a mesma coisa, porem essa de cima é mais comum
print(conteudo)



# open_file = open(nome_arquivo) # Abre arquivo em formato de leitura

# conteudo = open_file.read() # Lê os dados do arquivo
# print(conteudo)

# %%
# open_file.close() # Fechar o arquivo

