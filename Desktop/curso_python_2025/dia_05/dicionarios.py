# Dicionarios são pares de chave associado a um valor ou vice e versa

# Vamos usar muito isso em uma CHAMADA DE API (Application Programming Interface = Interface de Programação de Aplicações)

# Vamos usar muito isso em PANDAS
#(PANDAS é uma biblioteca do python para manipulação de dados)

# Em outras linguagens dicionario é conhecida como map

# %%

dados_milena = {
  "nome":"Milena",
  "sobrenome":"Silva",
  "filhos":False,
  "formacao":["arquitetura","analise e desenvolvimento de sistemas"],
  "cargos":[
    {"nome": "estagiaria", "empresa": "pedro jessen"},
    {"nome": "cooperadora", "empresa": "hannah larocerie"},
    {"nome": "cooperadora", "empresa": "priscilla camara"},
    {"nome": "arquiteta", "empresa": "nós arquitetura"} 
    ]
}

# %% 

print(dados_milena)
print(dados_milena["formacao"][-1])
print(dados_milena["cargos"][-2]["empresa"])

# %%

dados_milena["estado civil"] = "casada"

# %%

print(dados_milena)

# %%

print("Chaves:",dados_milena.keys())
print("Valores:",dados_milena.values())
print("Itens:", dados_milena.items()) # Lista de tuplas com as chaves e o seu valor

# %%

for i in dados_milena:
  print(i, "->", dados_milena[i])

# %%

for chave in dados_milena:
  print(chave, "->", dados_milena[chave])

  # %%

  for chaves, valor in dados_milena.items():
    print(chave, "->", valor)

# %%

for i in [10,20,45,28,"Téo"]:
  print(i) # Pecorre tudo que está nas chaves acima de maneira unitária

# %%

