##Questão 2
#Dado o Dicionário Animal com a seguinte estrutura: {"Especie": "Cachorro", "Raça": "Pinscher", "Idade": 1, "Adestrado": "Sim"},
#faça um programa que cheque se o cachorro tem mais de 2 anos de idade, se tiver, crie uma nova chave chamada "Vacinado" e atribua o valor de
#verdadeiro, caso contrário, mude o valor da chave "Adestrado" para "Não"

dicionario_animal = {"Especie": "Cachorro", "Raça": "Pinscher", "Idade": int(input("Digite a idade do animal: ")), "Adestrado": "Sim"}

if dicionario_animal["Idade"]> 2:
    dicionario_animal["Vacinado"] = True
else:
    dicionario_animal["Adestrado"] = "Não"

print(dicionario_animal)