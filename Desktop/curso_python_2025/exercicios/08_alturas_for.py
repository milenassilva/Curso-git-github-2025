# %%
#Faça um programa que receba 4 altura usando um laço
# de repetição e realize a soma dessas altura.

soma = 0          # valor final
qtde_entradas = 4 # o contador de entradas

for i in range(qtde_entradas):
  altura = input("Entre com a altura: ")
  altura = float(altura)
  soma += altura

print("Somas das alturas:", soma)

