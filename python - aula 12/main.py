class Gato:
    def __init__(self, nome:str, raca:str, peso:float, idade:int, castrado:bool):
        self.nome = nome
        self.raca = raca
        self.peso = peso
        self.idade = idade
        self.castrado = castrado

    def miar(self):
        return f"O {self.nome} está miando, dê atenção a ele."
    
gatinho1 = Gato(nome = "Garfield", raca = "Persa", peso = 8, idade = 6, castrado = True)
gatinho2 = Gato(nome = "Lisa", raca = "Angorá", peso = 6, idade = 2, castrado = False)

print(gatinho1.miar())
print(gatinho2.miar())