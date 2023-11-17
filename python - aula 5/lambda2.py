import datetime

ano_atual = datetime.datetime.now().year

maior_de_idade = lambda idade: f"tem {idade} anos e é maior de idade" if idade >= 18 else f"tem {idade} anos e é menor de idade"

year = int(input("Digite seu ano de nascimento: "))
idade = ano_atual - year


print(maior_de_idade(idade))

