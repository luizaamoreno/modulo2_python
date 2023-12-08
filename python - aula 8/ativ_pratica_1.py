numeros = []
contador = 0

while contador <= 10:
    contador += 1
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)
print(f"O programa gerou a lista: {numeros}.")


pares = []
for par in numeros:
    if par % 2 == 0:
        pares.append(par)

print(f"Os números pares da lista são: {pares}.")