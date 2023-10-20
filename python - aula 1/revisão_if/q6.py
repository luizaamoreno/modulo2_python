n1 = int(input("digite um número: "))
n2 = int(input("digite um número: "))

operacao = float(input("""
        Qual operação você deseja realizar?
            Digite 1 para soma
            Digite 2 para subtração
            Digite 3 para multiplicação
            Digite 4 para divisão
            """))

if operacao == 1:
    soma = n1 + n2
    if soma >= 0 and soma % 2 == 0:
        print(f"a soma dos números resulta em {soma} e num número positivo e par.")
    elif soma > 0 and soma % 2 != 0:
        print(f"a soma dos números resulta em {soma} e num número positivo e ímpar.")
    elif soma < 0 and soma % 2 == 0:
        print(f"a soma dos números resulta em {soma} e num número negativo e par.")
    elif soma < 0 and soma % 2 != 0:
        print(f"a soma dos números resulta em {soma} e num número negativo e ímpar.")
elif operacao == 2:
    subtracao = n1 - n2
    if subtracao >= 0 and subtracao % 2 == 0:
        print(f"a subtracao dos números resulta em {subtracao} e num número positivo e par.")
    elif subtracao > 0 and subtracao % 2 != 0:
        print(f"a subtracao dos números resulta em {subtracao} e num número positivo e ímpar.")
    elif subtracao < 0 and subtracao % 2 == 0:
        print(f"a subtracao dos números resulta em {subtracao} e num número negativo e par.")
    elif subtracao < 0 and subtracao % 2 != 0:
        print(f"a subtracao dos números resulta em {subtracao} e num número negativo e ímpar.")
elif operacao == 3:
    multiplicacao = n1 * n2
    if multiplicacao >= 0 and multiplicacao % 2 == 0:
        print(f"a multiplicacao dos números resulta em {multiplicacao} e num número positivo e par.")
    elif multiplicacao > 0 and multiplicacao % 2 != 0:
        print(f"a multiplicacao dos números resulta em {multiplicacao} e num número positivo e ímpar.")
    elif multiplicacao < 0 and multiplicacao % 2 == 0:
        print(f"a multiplicacao dos números resulta em {multiplicacao} e num número negativo e par.")
    elif multiplicacao < 0 and multiplicacao % 2 != 0:
        print(f"a multiplicacao dos números resulta em {multiplicacao} e num número negativo e ímpar.")
elif operacao == 4:
    divisao = n1/n2
    if divisao >= 0 and divisao % 2 == 0:
        print(f"a divisao dos números resulta em {divisao} e num número positivo e par.")
    elif divisao > 0 and divisao % 2 != 0:
        print(f"a divisao dos números resulta em {divisao} e num número positivo e ímpar.")
    elif divisao < 0 and divisao % 2 == 0:
        print(f"a divisao dos números resulta em {divisao} e num número negativo e par.")
    elif divisao < 0 and divisao % 2 != 0:
        print(f"a divisao dos números resulta em {divisao} e num número negativo e ímpar.")
else:
    print("você digitou uma informação inválida, tente novamente.")