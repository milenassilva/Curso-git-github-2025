
def soma(a:float, b:float, *args)->float: # args é um argumento para definir que pode ser que outros valores seja adicionado junto com o a e b, esse nome 'args' é opção pode ser qualquer outro, mas é mais comum usar esse. esses nomes floats não é obrigatorio mais é uma boa pratica usar para orientar quem vai usar o cod, pode ser int
  valores = [a,b] + list(args)
  return sum(valores)

def media(a:float, b:float, *args)->float:
  return soma(a, b, *args) / (len(args)+2)

a = float(input("Entre com o valor de a: "))
b = float(input("Entre com o valor de b: "))
c = float(input("Entre com o valor de c: "))
d = float(input("Entre com o valor de d: "))

print("Média", media(a,b,c,d))
