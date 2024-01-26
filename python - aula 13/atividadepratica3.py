class Aluno:
    def __init__(self, nome:str, idade:int, matricula:str):
        self.__nome = nome
        self.__idade = idade
        self.__matricula = matricula

    def getNome(self):
        return self.__nome
    
    def setNome(self, novo_valor):
        self.__nome = novo_valor
        return self.__nome
    
    def getIdade(self):
        return self.__idade
    
    def setIdade(self, novo_valor):
        self.__idade = novo_valor
        return self.__idade
    
    def getMatricula(self):
        return self.__matricula
    
    def setMatricula(self, novo_valor):
        self.__matricula = novo_valor
        return self.__matricula
    
