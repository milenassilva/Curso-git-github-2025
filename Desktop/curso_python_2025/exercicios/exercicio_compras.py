# Faça um programa que verifique se o item que a pessoa escolheu 
# para comprar na loja está na lista: laranja, cerveja, miojo, carvão, picanha.

item_loja = ["laranja", "cerveja", "miojo", "carvão", "picanha"]

produto = input("Digite aqui o item que deseja comprar: ")

if produto in item_loja :
  print("temos esse item em loja!")

else :
  print("Não temos esse item em estoque.")