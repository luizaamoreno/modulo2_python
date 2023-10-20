contador = 1

while contador <= 10:
    numero = int(input("Digite um número: "))
    contador += 1

if numero % 2 == 0:
    print(f"O {numero} é par")
else:
    print(f"o {numero} é ímpar")