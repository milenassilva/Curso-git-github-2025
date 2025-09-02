# %%
import requests                         # Request para realizar requisições na web

import json                             # json para tratar json de listas/dicionarios para arquivos

from tqdm import tqdm

import pandas as pd

ceps = [
    "01519000",
    "13329120",
    "21870370",
    "21645522",
    "13600110",
    "21051090",
    "14400760",
    "09656000",
    "01311902",
    "19060100",
    "53200351",
    "13175653",
    ]

url = "https://viacep.com.br/ws/{cep}/json" 

dados = []
for i in tqdm(ceps):
  resposta = requests.get(url.format(cep=i))        # Get é para obter, para consumir
  if resposta.status_code == 200:
    dados.append(resposta.json())                   # como o link que passamos está no formato de json pela estrutura de dicionario, chamamos a resposta, que é o link transformado em get que estamos consumindo os dados dessa API

dados

dataset = pd.DataFrame(dados)
dataset.to_csv("ceps.csv", sep=";")

with open("ceps.json", "w", encoding='utf-8') as open_file: # Abre um arquivo chamado "ceps.json" em modo de escrita "w", retiramos o erro de escrita com o encoding
  json.dump(dados, open_file, ensure_ascii=False, indent=4)


# %%
