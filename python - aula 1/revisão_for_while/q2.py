
numero = int(input("Digite um número inteiro entre 1 e 10: "))

if numero <= 0 or numero > 10:
    print("entrada inválida, tente novamente.")
else:
    tabuada = 0
    for i in range(1,11):
        tabuada += 1
        print(f"{numero} x {tabuada} = {numero*tabuada}")