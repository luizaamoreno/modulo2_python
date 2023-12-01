from numeros.numerais import *

while True:
    print("""AQUI ESTÁ SUA CALCULADORA:
        [1] SOMA
        [2] SUBTRAÇÃO
        [3] MULTIPLICAÇÃO
        [4] DIVISÃO
        [0] SAIR""")
    menu = int(input("Qual operação deseja realizar? "))
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
         
    match menu:
        case 1:
            print(f"O resultado é {soma(n1,n2)}.")
        case 2:
            print(f"O resultado é {subtracao(n1,n2)}.")
        case 3:
            print(f"O resultado é {multiplicacao(n1,n2)}.")
        case 4:
            print(f"O resultado é {divisao(n1,n2)}.")
        case 0:
            print("Até logo!")
            break
        case _:
            print("Opção inválida.")
