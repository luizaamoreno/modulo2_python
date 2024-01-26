class Tarefa:
    def __init__(self, descricao:str, prioridade:str, hora: int):
        self.descricao = descricao
        self.prioridade = prioridade
        self.hora = hora

class Projeto:
    def __init__(self, nome: str, meta: str, lista_tarefas: list):
        self.nome = nome
        self.meta = meta
        self.lista_tarefas = lista_tarefas

tarefa1 = Tarefa(descricao="Estudar SUS", prioridade="Alta", hora=21)
tarefa2 = Tarefa(descricao="Estudar Ingles", prioridade="Baixa", hora=20)
tarefa3 = Tarefa(descricao="Lavar a louça", prioridade="Média", hora=23)
tarefa4 = Tarefa(descricao="Ir para a academia", prioridade="Média", hora=14)

projeto1 = Projeto(nome="Projeto Anvisa 2024", meta="Passar no concurso", lista_tarefas=[tarefa1, tarefa2])
projeto2 = Projeto(nome="Projeto continuar gostosa", meta="não perder os resultados alcançados", lista_tarefas=tarefa4)
