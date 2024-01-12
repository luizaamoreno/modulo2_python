class Pessoa:
    def __init__(self, nome, idade, peso, genero):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.genero = genero



nome_entrada = str(input("Digite seu nome: "))
pessoa1 = Pessoa(nome=nome_entrada)