class Carro:
    def __init__(self, marca:str, cor:str, modelo:str, ano:int, qtde_portas:int):
        self.marca = marca
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.qtde_portas = qtde_portas

    def buzinar(self):
        return f"O {self.modelo} está buzinando."

carro1 = Carro(marca="Ford", cor="Preto", modelo="Ka", ano="2019", qtde_portas=4)
        
print(carro1.marca, carro1.modelo, carro1.cor)

print(carro1.buzinar())