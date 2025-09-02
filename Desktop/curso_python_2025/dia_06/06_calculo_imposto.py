# %%

def calc_imposto(preco:float, tx_base:float, **kwargs)->float: # kwargs se comprta com um dicionario, que la no final a gnt pode colocar a chave e o valor, sem alterar o codigo inteiro, como fiz com municio, estadual e poderia sair colocando varias outras chaves e valores que ele vai calcular sem alterar o codigo inteiro
  imposto = preco * tx_base

  for i in kwargs:
    print(i, kwargs(i))
    imposto += preco * kwargs[i]
  
  return imposto


# %%
impostos_gerais = {
  "municipal" : 0.01, 
  "estadual" : 0.005, 
  "nacional" : 0.001
}

calc_imposto(100, 0.03, **impostos_gerais) # Essa parte aqui é a mesma coisa que passar o codigo comentado abaixo, criou um dicionaria acima e colocou no parenteses só um nome para o codigo ficar mais organizado, mas pode ser feito como a linha abaixo comentada

# calc_imposto(100, 0.03, municipal=0.01, estadual=0.005, nacional=0.001) 
# # Os valores obrigatorios são os 2 primeiros, o restante são valores adicionados conforme 'necessidade' vamos dizer assim, e esse valores com suas chaves 'nomes' são armazenados no kwargs 

# %%
