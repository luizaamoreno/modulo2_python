produtos = [("Maçã", 2.50),("Banana", 1.75),("Laranja",3.00)]
soma = 0

for produto in produtos:
    soma += produto[1] #o [1] corresponde à posição do elemento dentro da tupla

print(soma)