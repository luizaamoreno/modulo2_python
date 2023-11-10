def IMC(peso, altura):
    return peso / altura**2

lista_IMCs = []

for i in range(4):
    nome = str(input("Digite seu nome: "))
    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))
    

    lista_IMCs.append([nome, IMC(peso, altura)])
   
#print(lista_IMCs)

for x in lista_IMCs:
    print(f"O IMC de {x[0]} é {x[1]}.")
