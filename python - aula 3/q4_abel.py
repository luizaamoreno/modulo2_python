#Questão 4
#Dado o dicionário Computador com a seguinte estrutura {"Processador": "I7", "Memoria": "16GB", "SSD": "256GB"}
#faça um programa que crie uma copia desse dicionário e  guarde ele em outra variável chamada Computador2
# e depois limpe o dicionario Computador

computador = {
    "Processador": "I7",
    "Memoria": "16GB",
    "SSD": "256GB"
    }

computador2 = computador.copy()

computador.clear()

print(computador)
print(computador2)