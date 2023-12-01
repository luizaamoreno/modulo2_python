# DENTRO DO MESMO PACOTE escola, CRIE UM MÓDULO CHAMADO português QUE TENHA DENTRO DELE AS FUNÇÕES:
# inverter_texto (QUE RECEBE UM TEXTO E RETORNA ELE INVERTIDO)
# contar_caracteres (QUE RECEBE UM TEXTO E RETORNA A QUANTIDADE DE CARACTERES DAQUELE TEXTO)
# contar_vogais_e_consoantes (QUE RECEBE UM TEXTO E RETORNA A QUANTIDADE DE VOGAIS E A QUANTIDADE DE CONSOANTES QUE AQUELE TEXTO TEM)

def inverter_texto(texto):
    invertido = texto[::-1]
    return invertido

def contar_caracteres(texto):
    caracteres = len(texto)
    return caracteres

def contar_vogais_e_consoantes(texto):
    contador_vogal = 0
    contador_consoante = 0
    for letra in texto:
        if letra.lower() in "aeiou":
            contador_vogal += 1
        elif letra.lower() in "bcdfghjklmnpqrstuvwxyz":
            contador_consoante +=1
    return {"vogais": contador_vogal,"consoantes": contador_consoante}