class Veiculos:
    def __init__(self, modelo: str, cor: str):
        self.modelo = modelo
        self.cor = cor

class Carro(Veiculos):
    def __init__(self, modelo: str, cor: str, qtd_portas: int):
        super().__init__(modelo, cor)
        self.qtd_portas = qtd_portas
    
class Bicicleta(Veiculos):
    def __init__(self, modelo: str, cor: str, aro: int):
        super().__init__(modelo, cor)
        self.aro = aro
    
