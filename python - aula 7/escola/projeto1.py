# CRIE UM PACOTE CHAMADO escola QUE CONTENHA UM MÓDULO CHAMADO matemática QUE TENHA DENTRO DELE AS FUNÇÕES:
# maior_numero (QUE RECEBE UMA LISTA DE NÚMEROS E RETORNA O MAIOR DELES)
# menor_numero (QUE RECEBE UMA LISTA DE NÚMEROS E RETORNA O MENOR DELES)
# media_numeros (QUE RECEBE UMA LISTA DE NÚMEROS E RETORNA A MÉDIA DELES)
# DENTRO DO MESMO PACOTE escola, CRIE UM MÓDULO CHAMADO português QUE TENHA DENTRO DELE AS FUNÇÕES:
# inverter_texto (QUE RECEBE UM TEXTO E RETORNA ELE INVERTIDO)
# contar_caracteres (QUE RECEBE UM TEXTO E RETORNA A QUANTIDADE DE CARACTERES DAQUELE TEXTO)
# contar_vogais_e_consoantes (QUE RECEBE UM TEXTO E RETORNA A QUANTIDADE DE VOGAIS E A QUANTIDADE DE CONSOANTES QUE AQUELE TEXTO TEM)
# obs: pode retornar uma lista ou um dicionário com os dois valores

infinito_positivo = float("inf")
infinito_negativo = -float("inf")

lista_numeros = []

while True:
    print("""Módulo:
          [1] MATEMÁTICA
          [2] PORTUGUÊS)""")
    modulo = int(input("Digite a opção desejada: "))
        

    numero = int(input("Digite um número inteiro: "))
    lista_numeros.append(numero)
    if numero == 22:
        break
print(lista_numeros)





    # confirmar = str(input("Deseja continuar? [S/N]: "))
    # if confirmar.lower() == "s":
    #     continue
    # elif confirmar.lower() == "n":
    #     break
    # else: 
    #     print("Resposta inválida.")