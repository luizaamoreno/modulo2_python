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

def cadastrar_aluno():
    aluno = {'nome' : }

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