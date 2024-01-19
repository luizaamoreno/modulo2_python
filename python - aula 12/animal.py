class Animal:
    def __init__(self, nome:str, raca:str, idade:int, cor:str):
        self.nome = nome
        self.raca = raca
        self.idade = idade
        self.cor = cor
    
    def emitir_som(self):
        return "Som indefinido."
    
class Gato(Animal):
    def __init__(self, nome: str, raca: str, idade: int, cor: str):
        super().__init__(nome, raca, idade, cor)
    
    def emitir_som(self):
        return "Miauuuuu"

class Cachorro(Animal):
    def emitir_som(self):
        return "Au Au"
    
gatim = Gato(nome="Xaninho", raca="dos preto", idade=6, cor="branco")
cachorrim = Cachorro(nome="Scooby", raca="Vira-lata", idade=4, cor="Caramelo")
porco = Animal(nome="Bacon", raca="Dos fofim", idade=1, cor="rosa")

print(gatim.emitir_som())
print(cachorrim.emitir_som())
print(porco.emitir_som())