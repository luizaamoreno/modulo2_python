from matematica import *
from portugues import *

lista_de_notas = []
for i in range(4):
    nota = float(input("Digite uma nota: "))
    lista_de_notas.append(nota)

print(f"o maior número é {maior_numero(lista_de_notas)}.")
print(f"O menor número é {menor_numero(lista_de_notas)}.")
print(f"A média dos números é {media_numeros(lista_de_notas)}.")

palavra = str(input("Digite uma palavra: "))
invertida = inverter_texto(palavra)
resposta = contar_vogais_e_consoantes(palavra)
if palavra == invertida:
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")
print(f"A palavra {palavra} possui {resposta['consoantes']} consoantes e {resposta['vogais']} vogais.")
