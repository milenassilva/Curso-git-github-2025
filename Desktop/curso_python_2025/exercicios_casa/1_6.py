# Faça um programa que receba um número em segundos, 
# converta esse número para horas, minuto e segundos. 
# Exemplos:
# Entrada: 556
# Saída: 0:9:16
# Entrada: 140153
# Saída: 38:55:53

segundos = int(input("Entre com os segundos: "))

horas = segundos // 3600 
resto = segundos % 3600
minutos = resto // 60
segundos_finais = resto % 60

print(f"{horas}:{minutos}:{segundos_finais}")
