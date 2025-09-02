# Faça um programa que receba um número inteiro
# e calcule sua raiz quadrada e exiba o resultado

numero =  input("Entre com um numéro inteiro para saber a raiz quadrada: ")
numero = int(numero)

raiz = numero ** (1/2) 
print("A raiz quadrada de", numero, "é:", raiz)