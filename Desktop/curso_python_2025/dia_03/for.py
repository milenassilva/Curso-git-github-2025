# %%
nome = "Milena Silva"

for letra in nome:
  print(letra)

# %%

numero = 2
max_numero = 100

for i in range(1, max_numero+1):
  print(numero, "x", i, "=", numero * i)

 # %%

# Quais são os numeros divisiveis por 4 no intervalo de 4 até 100

for i in range(4, 101):
  if i % 4 == 0:
    print(i)
