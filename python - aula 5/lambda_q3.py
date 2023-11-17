maior_que10 = lambda x: f"{x}" if x > 10 else f"{x/2}"

numero = int(input("digite um número inteiro: "))

print(maior_que10(numero))