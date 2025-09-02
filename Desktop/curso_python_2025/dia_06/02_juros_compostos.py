# %%

def juros_compostos(aporte:int, taxas:float, anos:int)->float:
     
     """juros_compostos serve para calcular o retorno financeiro apartir de uma aporte. Deve-se considerar o valor, a taxa de juros atual e o tempo (em anos) para cálculo do valor a ser retornado.

  aporte:
      Um número inteiro, que represente o valor em R$

  taxa:
      Um número float entre 0 e 1 que represente o valor taxa de juros

  anos:
      Um número inteiro >=1 que represente o tempo que o invetimento terá liquidez
      """
     return aporte * (1 + taxas) ** anos 
 

# $$

juros_compostos(aporte=1000, taxas=0.13, anos=4)

# %%
print()