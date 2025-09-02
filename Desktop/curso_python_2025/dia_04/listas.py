# %%

# Uma maneira de definir listas
idades = [28, 42, 43, 35, 39, 28, 38]

print(idades)

# %%
Milena = ["Milena", "Silva", 31, False, "casada", 1050.98]

#idade
print(Milena[2])

#renda
print(Milena[5])

#Nome
print(Milena[0])

# %%

idades = [28, 42, 43, 35, 39, 28, 38, 42]

print("Soma das idades:", sum(idades))

print("Quantidade idades:", len(idades))

print("Média das idades:", sum(idades)/len(idades))

print("Menor idade:", min(idades))

print("Maior idade:", max(idades))

# %%

Milena = ["Milena Silva", 31, False, "Casada", ["estagiária", "arq jr.", "arq pl", "arquiteta"], [1500, 4000, 4500, 6500, 10000], ["Ana", "Gaby", "Dani"]]

print("Tamanho de Milena", len(Milena))

print(Milena[6][0])

amgs = Milena[6]
primeira_amg = amgs[0]
print(primeira_amg)

# %%

tamanho = len(Milena)
pos = tamanho - 1
amgs = Milena[pos]

Milena[pos][len(amgs)-1]
# %%

Milena[-1][-1]
# %%
# Primeiros 4 elementos
Milena[0:4]

# %%
Milena[4][2:4]

# %%
Milena[4][-2:]

# %%

Milena[:4]

# %%
# Milena[ start : stop ]

# %%

salarios = Milena[5]
salarios[::2]

# Milena[ start : stop : step ]
# %%
