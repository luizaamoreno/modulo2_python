#faça um programa que pede para o usuário cadastrar 5 alunos com nome e nota e no final mostra o nome e nota do aluno que tirou a maior nota:

alunos = []

maior = 0

for i in range(5):
    aluno = str(input("Aluno: "))
    nota = float(input("Nota: "))
    
    alunos.append([aluno, nota])

maior_nota = 0
aluno_top = ""

for aluno in alunos:
    if aluno[1] > maior_nota:
        maior_nota = aluno[1]
        aluno_top = aluno[0]
    
print(f"O aluno que tirou a maior nota ({maior_nota}) foi {aluno_top}.")