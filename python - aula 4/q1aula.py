#FAÇA UMA FUNÇÃO QUE RECEBE 2 NÚMEROS E RETORNA O MAIOR DO DOIS

def maior(n1, n2):
    if n1 > n2:
        return n1
    elif n2 > n1:
        return n2
    else:
        return "São iguais."

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite mais um número: "))

print(maior(numero1, numero2))

def maior(n1:int, n2:int):
    if n1 > n2:
        return n1
    elif n2 > n1:
        return n2
    else:
        return "São iguais."

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite mais um número: "))

print(f"O {maior(numero1, numero2)} é o maior número.")