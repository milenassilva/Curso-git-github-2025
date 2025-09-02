
# Faça um programa que vende uma garrafa de água?
# Se o cliente escolher água mineral natura, será cobrado R$1,50
# Se o cliente escolher água moneral com gás, será cobrado R$2,50

texto = """
Escolha a opção desejada:
(1) Água mineral natural
(2) Água mineral com gás
"""

opcao = input(texto)

if opcao == "1":
  print("Total a pagar R$ 1,50")

elif opcao == "2":
  print("Total a pagar R$ 2,50")

else :
  print("Digite uma opção válida por favor.")