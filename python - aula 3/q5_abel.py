#Questão 5
#Dado a lista ["Banda", "Musica"], crie apartir dessa lista um #dicionário  e depois insira na key Banda o valor "Iron Maiden", e no #campo "Música" o valor "Powerslave", 
#depois faça uma busca nesse #objeto criado Cuja busca irá buscar por duas chaves diferentes, uma #chave chamada Banda  e outra chave chamada "Integrantes", 
#caso a chave #exista dentro do dicionário mostre ela na tela, caso não existe mostra #uma mensagem informando que a chave procurada não existe.

lista = ["Banda", "Musica"]

dicionario = dict.fromkeys(lista)

dicionario["Banda"] = "Iron Maiden"
dicionario["Musica"] = "Powerslave"

print(dicionario.get("Banda", "Chave não existe"))
print(dicionario.get("Integrantes", "Chave não existe"))

print(dicionario)

