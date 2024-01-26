def adicionar_produto(lista_produtos, nome, quantidade, valor_unitario):
    total_produto = quantidade * valor_unitario
    produto = {"produto": nome,
               "quantidade": quantidade,
               "valor": valor_unitario,
               "total": total_produto}
    lista_produtos.append(produto)
    return total_produto

def ver_lista(lista_produtos):
    print("\nLista de Produtos:")
    for produto in lista_produtos:
        print(f"{produto['produto']} - Quantidade: {produto['quantidade']}, Valor Unitário: {produto['valor']}, Total: {produto['total']}")
    
    valor_total = 0
    for produto in lista_produtos:
        valor_total = valor_total + produto['total']
    print(f"\nValor Total de Todos os Produtos: {valor_total}\n")

def atualizar_produto(lista_produtos, nome_produto):
    for produto in lista_produtos:
        if produto['produto'] == nome_produto:
            print(f"\nProduto encontrado. Atualize as informações:")
            produto['produto'] = input("Novo Nome do Produto: ").upper().strip()
            produto['quantidade'] = int(input("Nova Quantidade: "))
            produto['valor'] = float(input("Novo Valor Unitário: "))
            produto['total'] = produto['quantidade'] * produto['valor']
            print("Produto atualizado com sucesso.\n")
            return
    print(f"Produto '{nome_produto}' não encontrado na lista.\n")

def remover_produto(lista_produtos, nome_produto):
    for produto in lista_produtos:
        if produto['produto'] == nome_produto:
            lista_produtos.remove(produto)
            print(f"\nProduto '{nome_produto}' removido com sucesso.\n")
            return
    print(f"Produto '{nome_produto}' não encontrado na lista.\n")

lista_produtos = []
total_produtos = 0

while True:
    print(""" 
    ** Menu: **
    1. Adicionar Produto
    2. Ver Lista de Produtos
    3. Atualizar Produto
    4. Remover Produto
    5. Encerrar Programa
            """)

    opcao = input("Escolha uma opção (1-5): ")

    if opcao == "1":
        nome_produto = input("Nome do Produto: ").upper().strip()
        quantidade = int(input("Quantidade: "))
        valor_unitario = float(input("Valor Unitário: "))
        total_produtos += adicionar_produto(lista_produtos, nome_produto, quantidade, valor_unitario)
        print("Produto adicionado com sucesso.\n")

    elif opcao == "2":
        if len(lista_produtos) == 0:
            print("""
A lista está vazia, adicione pelo menos um produto.
                    """)
        else:
            ver_lista(lista_produtos)

    elif opcao == "3":
        nome_produto = input("Digite o nome do produto que deseja atualizar: ").upper().strip()
        atualizar_produto(lista_produtos, nome_produto)

    elif opcao == "4":
        nome_produto = input("Digite o nome do produto que deseja remover: ").upper().strip()
        remover_produto(lista_produtos, nome_produto)

    elif opcao == "5":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida. Tente novamente.\n")
