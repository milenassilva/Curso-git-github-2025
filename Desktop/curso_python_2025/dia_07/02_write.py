# %%
txt = "Meu novo arquivo de texto\n" # dentro do arquivo vai ta escrito isso. o \n é uma quebra de linha, para se caso eu quiser escrever algo a mais, não fique o texto grudado

nome_arquivo = "historia_02.txt" # Aqui é o nome do arquivo, pode ser qualquer um que voce quiser

with open(nome_arquivo, mode="w") as open_file:
  open_file.write(txt)
# Aqui ta criando o arquivo, abrindo o arquivo e definindo se o arquivo é um arquivo de escrita ou de leitura, isso define no mode="", se colocar "a" quer dizer que é de escrita, mas não vai excluir ou escrever por cima oq já tem no arquivo. se colocarmos "w" escreve, mas escreve por cima do que já tem, mas precisa colocar ele para a primeira atualização. se colocar "r" diz que p arquivo é de leitura.
# %%
