def somar(n1:float,n2:float):
    return n1 + n2

def subtrair(n1:float, n2:float):
    return n1 - n2

def multiplicar(n1:float, n2:float):
    return n1*n2

def dividir(n1:float, n2:float):
    return n1/n2

while True:
    n1 = float(input("Digite um número: "))
    n2 = float(input("Digite outro número: "))
    
    op = int(input("""
        Qual operação você deseja realizar?
        [1] Somar
        [2] Subtrair
        [3] Multiplicar
        [4] Dividir
        [5] Sair
        
        Digite somente o número: """))
    
    if op == 1:
        print(f"A soma dos números resulta em {somar(n1,n2)}.")
    elif op == 2:
        print(f"A subtração dos números resulta em {subtrair(n1,n2)}.")
    elif op == 3:
        print(f"A multiplicação dos números resulta em {multiplicar(n1,n2)}.")
    elif op == 4:
        if n2 == 0:
            print("Essa divisão não é possível pois o denominador é 0.")
        else:
            print(f"A divisão dos números resulta em {dividir(n1,n2)}.")
    elif op == 5:
        print("Até logo!")
        break
    else:
        print("Você digitou uma entrada inválida, tente novamente.")
