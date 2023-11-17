par_impar = lambda x: f"o numero {x} é par." if x % 2 == 0 else f"o numero {x} é ímpar."

user_n = int(input("Digite um número inteiro: "))

print(par_impar(user_n))