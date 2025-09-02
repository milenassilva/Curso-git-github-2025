# Faça um programa que receba um número. Verifique se este número é primo ou não, e retorne o resultado:
#   O número x é primo
#   O número x não é primo

numero = int(input("Digite um número: "))

divisores = 0  # vai contar quantas vezes o número é divisível

# vamos testar todos os números de 1 até ele mesmo
for i in range(1, numero + 1):
    if numero % i == 0:   # se dividir certinho
        divisores = divisores + 1

# um número primo tem exatamente 2 divisores: 1 e ele mesmo
if divisores == 2:
    print("O número", numero, "é primo")
else:
    print("O número", numero, "não é primo")