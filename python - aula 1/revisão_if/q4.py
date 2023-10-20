alfabeto = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
vogal = 'aeiouAEIOU'

letra = str(input("digite uma letra: ")).lower().strip()

while True:
    letra = str(input("digite uma letra: "))
    if letra in vogal:
        print(f"a letra {letra} é uma vogal.")
    elif letra in alfabeto:
        print(f"a letra {letra} é uma consoante.")
    else: 
        print(f"a letra {letra} é um número ou caractere especial.")