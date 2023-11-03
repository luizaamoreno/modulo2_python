#faça um programa que pede para o usuário inserir o nome de um aluno e a nota desse mesmo aluno e adicione ele a uma lista, até o usuário escrever no lugar do nome a palavra "fim".
#Então mostre na tela o nome do aluno que obteve a melhor nota.

alunos_nota = []
maior = 0

while True:
    nome = str(input("Digite o nome do aluno: ")).upper().strip()
    if nome == "FIM":
        print(alunos_nota)
        break
    nota = float(input("Digite a nota do aluno: "))
    
    alunos_nota.append([nome, nota])

maior_nota = 0
aluno_top = ""

for aluno in alunos_nota:
    if aluno[1] > maior_nota:
        maior_nota = aluno[1]
        aluno_top = aluno[0]

print(f"o aluno que tirou a maior nota ({maior_nota}) foi {aluno_top}.")
