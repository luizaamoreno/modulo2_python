#faça um programa que peça o nome de 5 pessoas e as adiciona em uma lista. Ao final, essa lista é mostrada. Depois, faça o usuário escolher uma posição e um novo membro para 
#a lista e adicione esse novo membro na posição escolhida pelo usuário.(USAR O INSERT)


contador = 1
grupo = []

while contador <=5:
    nome = str(input("Adicione alguém ao grupo: "))
    grupo.append(nome)
    contador += 1

answer = int(input(f""" 
      A lista ficou assim: {grupo}, deseja adicionar mais alguém?
      Digite 1 para SIM ou
      Digite 2 para NÃO
      """))

if answer == 1:
    adicionar = str(input("Qual nome da pessoa? "))
    posicao = int(input(f""" Em que posição deseja adicioná-la? Digite um número entre 1 a {len(grupo)+1}. 
                        """))
    grupo.insert(posicao - 1, adicionar)
    print(f"Grupo fechado: {grupo}")
elif answer == 2:
    print(f"grupo fechado: {grupo}")
else:
    print("entrada inválida. Você deve digitar 1 para SIM ou 2 para NÃO.")