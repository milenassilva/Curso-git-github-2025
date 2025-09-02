#Faça um programa que receba o raio de uma circunferência em centímetros. 
# Retorne para o usuário qual é a área e perímetro desta circunferência no seguinte formato.
# Área:  x.xx
# Perímetro:  y.yy

raio = input("Digite o valor de uma raio para saber sua área e seu perimetro:")
raio = float(raio)

area = 3.14 * raio * raio
perimetro = (2 * 3.14) * raio
perimetro = round(perimetro,2)

print("Área:", area)
print("Perimetro:", perimetro)