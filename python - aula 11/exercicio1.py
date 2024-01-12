#cria uma classe chamado moto que tenha os atributos: marca, modelo, cilindradas e cor
#Instancie 3 motos e mostre na tela:
# a marca da primeira moto
# as cilindradas e a cor da segunda moto
# todas as infos da terceira moto

class Moto:
    def __init__(self, marca:str, modelo: str, cor:str, cilindradas:int):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.cilindradas = cilindradas
    
    def ligar(self):
        return f"A moto {self.modelo} ligou."
    
    def ver_informacoes(self):
        return f"""
        Marca: {self.marca}
        Modelo: {self.modelo}
        Cilindradas: {self.cilindradas}
        Cor: {self.cor}
           """
    
moto1 = Moto(marca="YAMAHA", modelo="XMAX ABS", cor = "azul", cilindradas=250)
moto2 = Moto(marca="BMW", modelo="G310 GS", cor = "branca", cilindradas=313)
moto3 = Moto(marca="Vespa", modelo="Piaggio Vespa", cor = "cobre", cilindradas=155)

print(f"""
Marca da primeira moto: {moto1.marca}

Cor da segunda moto: {moto2.cor}
Cilindradas da segunda moto: {moto2.cilindradas}

Marca da terceira moto: {moto3.marca}
Modelo da segunda moto: {moto3.modelo}
Cilindradas da segunda moto: {moto3.cor, moto3.cilindradas}

""")

print(moto1.ligar())
print(moto2.ligar())
print(moto3.ligar())

print(moto1.ver_informacoes())
print(moto2.ver_informacoes())
print(moto3.ver_informacoes())

