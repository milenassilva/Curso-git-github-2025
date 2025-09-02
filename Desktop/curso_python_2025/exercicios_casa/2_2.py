# Faça um programa que receba um número. 
# Verifique se o número informado é par ou ímpar. 
# Exiba o resultado da seguinte maneira:
# O número x é impar
# O número x é par

numero = int(input("Digite um número: "))
divisao = numero % 2

if divisao == 0:
  print("O número", numero,"é par")

else:
  print("O número", numero,"é impar")
