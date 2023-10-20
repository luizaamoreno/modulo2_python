soma = 0

for i in range(1,5):
    nota = int(input(f"Qual foi a nota da prova {i} do aluno? "))
    soma += nota

media = soma/4

if media >= 7 and media < 10:
    print("APROVADO")
elif media < 7:
    print("REPROVADO")
elif media == 10:
    print("Aprovado com DISTINÇÃO")