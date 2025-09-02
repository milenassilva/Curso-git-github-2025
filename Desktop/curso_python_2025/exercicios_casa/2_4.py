# Faça um programa que receba 4 notas de um aluno. 
# Retorne a média dessas notas, a menor e a maior nota:
#   Média: x
#   Menor: y
#   Maior: z

notas = []

for i in range(4):
  nota = float(input("Digite uma nota: "))
  notas.append(nota)

media = sum(notas) / len(notas)
menor = min(notas)
maxima = max(notas)

print("Media das notas:", media)
print("Nota minima:", menor)
print("Nota maxima:", maxima)