# Faça um programa que vende uma garrafa de água?
# Se o cliente escolher água mineral natura, será cobrado R$1,50
# Se o cliente escolher água moneral com gás, será cobrado R$2,50

# %%
texto = """
Escolha a sua água para comprar:
(1) Água mineral natural
(2) Água mineral com gás
"""
opcao = input(texto)

if opcao == "1":
  print("Sua conta deu: R$1,50")

elif opcao == 2:
  print("Sua conta deu: R$2,50")

else:
  print("Entre com a opção indicada, por favor.")

# %%

opcao = input(texto)

conta = 0
if opcao == "1":
  conta = 1.5
elif opcao == "2":
  conta = 2.5

if conta == 0:
  print("Entre com a opção indicada, por favor.")
else:
  print("Sua conta é: R$", conta)
  