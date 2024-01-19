from datetime import datetime

class Funcionario:
    def __init__(self, nome: str, cpf: str, idade: int):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
    
    def bater_ponto(self, horario):
        horario = datetime.now()
        horario_formatado = horario.strftime("%H:%M")
        return f"O {self.nome} bateu o ponto {horario_formatado} horas."

class Gerente(Funcionario):
    def __init__(self, nome: str, cpf: str, idade: int):
        super().__init__(nome, cpf, idade)

    def demitir(self):
        return f"O gerente {self.nome} demitiu alguém!"
    
    def contratar(self):
        return f"O gerente {self.nome} contratou alguém."
    
class Caixa(Funcionario):
    def __init__(self, nome: str, cpf: str, idade: int, num_caixa: int):
        super().__init__(nome, cpf, idade)
        self.num_caixa = num_caixa

    def fechar_caixa(self):
        return f"O {self.nome} fechou o caixa {self.num_caixa}."
    
gerente = Gerente(nome="Alberto", cpf="12345678900", idade=40)
caixa = Caixa(nome="Pedro", cpf="78945612300", idade=21, num_caixa=8)

print(gerente.contratar())
print(gerente.demitir())
print(gerente.bater_ponto(17))

print(caixa.fechar_caixa())
print(caixa.bater_ponto(18))

