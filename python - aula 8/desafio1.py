# FAÇA UM PROGRAMA DE SORTEIO DE CLIENTES ONDE O PROGRAMA VAI CADASTRANDO CLIENTES ATÉ O PROPRIO USUÁRIO DECIDIR QUE QUER PARAR(LOOP INFINITO)
# OS DADOS PARA CADASTRO SÃO: nome, cpf, valor_compra
# QUANDO O USUÁRIO ENCERRAR O LOOP FAÇA UM SORTEIO ENTRE TODOS OS CLIENTES CADASTRADOS E MOSTRE NA TELA TODOS OS DADOS DO CLIENTE QUE FOI SELECIONADO COM UMA MENSAGEM CUSTOMIZADA TIPO:
# """Parabéns {nome do cliente}, cpf: {cpf do cliente} você foi o sorteado por ter feito uma compra no valor de {valor da compra do cliente}"""

import random

lista_clientes = []
while True:
    novo_cadastro = str(input("Deseja cadastrar novo cliente? Digite S | N: ")).upper().strip()
    if novo_cadastro == "N":
        print("Vamos para o sorteio!")
        break
    elif novo_cadastro == "S":
        cliente = {
            'nome' : str(input("Digite seu nome: ")),
            'CPF' : int(input("Digite seu CPF: ")),
            'valor_compra' : float(input("Digite o valor da compra: ")),
    }
        lista_clientes.append(cliente)
    else:
        print("Você digitou uma opção inválida. Digite S para SIM ou N para NÃO.")

if lista_clientes == []:
    print("A lista está vazia, não é possível realizar o sorteio.")
else:
    cliente_sorteado = random.choice(lista_clientes)
    print(f"Parabéns, {cliente_sorteado['nome']}, CPF: {cliente_sorteado['CPF']}, você foi sorteado por ter feito uma compra no valor {cliente_sorteado['valor_compra']}.")

    print(f"Os clientes participantes foram: {lista_clientes}.")