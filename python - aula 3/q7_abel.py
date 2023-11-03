#Dado o conjunto Modulos com a seguinte estrutura {"Lógica de progamação", "Python", "HTML e CSS", "Javascript"}
#faça um programa que peça ao usuário o nome de um novo módulo e adicione esse módulo dentro desse conjunto

modulos = {"Lógica de programação" , "Python" , "HTML e CSS" , "Javascript"}

novo_modulo = str(input("Digite um novo módulo: "))
modulos.add(novo_modulo)

print(modulos)