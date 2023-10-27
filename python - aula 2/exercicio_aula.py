#faça um programa que peça o nome de 5 pessoas e as adiciona em uma lista. Ao final, essa lista é mostrada.

contador = 1
grupo = []

while contador <=5:
    nome = str(input("Adicione alguém ao grupo: "))
    grupo.append(nome)
    contador += 1

print(grupo)

lista = []

for i in range(5):
    nome = str(input("adicione alguém à lista: "))
    lista.append(nome)

print(lista)

grupao = []
while len(grupao) < 5:
    nomes = str(input("adicione alguém ao grupão: "))
    grupao.append(nomes)

print(grupao)