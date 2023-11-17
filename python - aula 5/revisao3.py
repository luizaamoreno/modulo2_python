
def maior_palavra(list_of_words):
    maior = ""
    for item in list_of_words:
        if len(item)> len(maior):
            maior = item
    return maior



lista_palavras = []

quantidade = int(input("Digite quantos nomes deseja inserir: "))

for i in range(quantidade):
    palavra = str(input("digite uma palavra: ")).strip()
    lista_palavras.append(palavra)

# while True:
#     palavra = str(input("digite uma palavra: ")).strip()
#     if palavra == "sair":
#         break
#     lista_palavras.append(palavra)


print(f"a maior palavra da lista digitada é {maior_palavra(lista_palavras)}.")