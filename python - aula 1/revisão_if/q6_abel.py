n1 = int(input("digite um número: "))
n2 = int(input("digite um número: "))

resultado = 0

operacao = int(input("""
        Qual operação você deseja realizar?
            Digite 1 para soma
            Digite 2 para subtração
            Digite 3 para multiplicação
            Digite 4 para divisão
            """))

if operacao == 1:
    resultado = n1 + n2
elif operacao == 2:
    resultado = n1 - n2
elif operacao == 3:
    resultado = n1*n2
elif operacao == 4:
    resultado = n1 / n2
else: 
    print("Entrada inválida. Tente novamente.")

if resultado % 2 == 0:
    print(f"{resultado} é par")
else:
    print(f"{resultado} é ímpar")


if resultado > 0:
    print(f"{resultado} é positivo")
elif resultado < 0:
    print(f"{resultado} é negativo")
else:
    print(f"{resultado} é neutro")
