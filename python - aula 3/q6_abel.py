colecao_cores = {"amarelo" , "azul" , "vermelho" , "verde"}

lista_novas_cores = []

while True:
    cor = (str(input("Escolha uma cor: ")))
    if cor == "sair":
        break
    lista_novas_cores.append(cor)


colecao_cores.update(lista_novas_cores)
print(colecao_cores)