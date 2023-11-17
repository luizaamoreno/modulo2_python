funcao = lambda x,y: f"{x}{y}" if len(x) > 5 and len(y) > 5 else "não foi possível juntar as palavras"

palavra1 = str(input("Nome: "))
palavra2 = str(input("Sobrenome: "))

print(funcao(palavra1,palavra2))