# FAÇA UM PROGRAMA DE CADASTRO DE ALUNOS, COM UM MENU COM AS OPÇÕES:
# 1 - Cadastrar aluno
# 2 - Visualizar alunos cadastrados
# 3 - Deletar Aluno
# 0 - Sair
# PARA CADASTRAR O ALUNO DEVE-SE PEDIR OS DADOS:
# nome, cpf, turma, notas (4 NOTAS) e GUARDAR ISSO EM UM DICIONÁRIO
# VISULIZAR MOSTRA TODOS OS ALUNOS CADASTRADOS EM UM PRINT CUSTOMIZADO:
# """
# Nome: {nome do aluno}
# CPF: {cpf do aluno}
# Turma: {turma do aluno}
# Nota 1: {primeira nota do aluno}
# Nota 2: {segunda nota do aluno}
# ...
# DELETAR ALUNO DEVE PERGUNTAR QUAL ALUNO SERÁ EXCLUIDO E REMOVE-LO DA LISTA DE ALUNOS

lista_alunos = []

def cadastrar_aluno():
    nome = str(input("Nome: "))
    cpf = int(input("CPF: "))
    turma = str(input("Turma: "))
    lista_notas = []
    for i in range(1,5):
        nota = float(input(f"Digite a {i}ª nota: "))
        lista_notas.append(nota)

    aluno = {'nome' : nome,
             'cpf': cpf,
             'turma' : turma,
             'notas' : lista_notas
    }
    lista_alunos.append(aluno)


def visualizar_alunos():
    for aluno in lista_alunos:  
        notas = aluno['notas']  
        print(f"""
        Nome: {aluno['nome']}
        CPF: {aluno['cpf']}
        Turma: {aluno['turma']}
        Nota 1: {notas[0]}
        Nota 2: {notas[1]}
        Nota 3: {notas[2]}
        Nota 4: {notas[3]}
        
           """) 

def deletar_aluno():
    remover = str(input("Qual nome do aluno deseja deletar? "))
    lista_alunos.pop(remover)

while True:
    print("""O que deseja acessar? 
    1 - Cadastrar aluno
    2 - Visualizar alunos cadastrados
    3 - Deletar Aluno
    0 - Sair
    """)
    opcao = int(input("Digite a opção escolhida: "))
    if opcao == 0:
        print("Até logo!")
        break
    elif opcao == 1:
        cadastrar_aluno()
    elif opcao == 2:
        if lista_alunos == []:
            print("Ainda não há alunos cadastrados.")
        else:
            visualizar_alunos()
    elif opcao == 3:
        deletar_aluno()
    else:
        print("Você digitou uma opção inválida. Escolha entre as disponíveis.")