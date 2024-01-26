class Autor:
    def __init__(self, nome: str, idade:int, nacionalidade:str):
        self.nome = nome
        self.idade = idade
        self.nacionalidade = nacionalidade

class Livro:
    def __init__(self, titulo: str, autor: Autor, genero: str, qtd_paginas: int):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.qtd_paginas = qtd_paginas

autor1 = Autor(nome="João", idade=52, nacionalidade="Brasileiro")
livro1 = Livro(titulo="Historia do João", autor=autor1, genero="Drama", qtd_paginas=200)

print(livro1.titulo)
print(livro1.autor.nacionalidade)