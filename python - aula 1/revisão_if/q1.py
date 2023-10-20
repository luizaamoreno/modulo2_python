#Faça um Programa que peça dois números ao usuário e imprima o maior deles.

# n1 = int(input("digite um número: "))
# n2 = int(input("digite um número: "))

# if n1 >= n2 and n1 >= n3:
#     print(f"{n1} é o maior número.")
# elif n2 >= n1 and n2 >= n3:
#     print(f"{n2} é o maior número")

# contador = 1

# while contador <= 2:
#     n = int(input("Digite um número: "))
#     if contador == 1:
#         maior = n
#     elif n > maior:
#         maior = n
#     contador +=1

# print(f"O maior número é {maior}.")

for i in range(1,3):
    n = int(input("digite um número: "))
    if i == 1:
        maior = n
    elif n > maior:
        maior = n

print(f"o maior número é {maior}.")