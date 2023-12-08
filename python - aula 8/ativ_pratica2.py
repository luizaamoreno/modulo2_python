# Crie um dicionário com informações de produtos, incluindo nome, preço e quantidade em estoque.
# Implemente funções para adicionar, remover e atualizar produtos no dicionário.

def adicionar_produto():
    estoque = []
    while nome != 'FIM':
        nome = str(input("Descrição: ")).upper()
        adicionar_produto = {
        'nome' : nome,
        'preço' : float(input("Preço: ")),
        'cor' : str(input("Cor: ")),
        'quantidade' : int("Quantidade: ")
        }
        estoque.append(adicionar_produto)


produto = {
    'nome' : 'garrafa',
    'preço' : 49.99,
    'cor' : 'rosa',
    'quantidade' : 5
    }

