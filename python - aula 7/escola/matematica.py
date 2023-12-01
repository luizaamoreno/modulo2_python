# maior_numero (QUE RECEBE UMA LISTA DE NÚMEROS E RETORNA O MAIOR DELES)
# menor_numero (QUE RECEBE UMA LISTA DE NÚMEROS E RETORNA O MENOR DELES)
# media_numeros (QUE RECEBE UMA LISTA DE NÚMEROS E RETORNA A MÉDIA DELES)

def maior_numero(numeros):
    maior = numeros[0]
    for numero in numeros:
        if numero > maior:
            maior = numero
    return maior

def menor_numero(numeros):
    menor = numeros[0]
    for numero in numeros:
        if numero < menor:
            menor = numero
    return menor

def media_numeros(numeros):
    soma = 0
    for numero in numeros:
        soma += numero
        media = soma / len(numeros)
    return media



# infinito_negativo = -float("inf")