#Questão 1
#Dado O Dicionário pessoa com a seguinte estrutura: {"Nome": "Abel", "Idade": 28, "Altura": 1.79, "Habilitacao": True},
#faça um programa que imprima na tela quantas chaves existem nesse dicionário, e quais os nomes de cada uma delas:

dicionario_pessoa = {
    "nome" : "LUIZA",
    "idade" : 31,
    "altura"  : 1.59,
    "habilitacao" : True,
}

print(f"o dicionário possui {len(dicionario_pessoa)} chaves.")

lista_chaves = list(dicionario_pessoa)

for chaves in lista_chaves:
    print(chaves)