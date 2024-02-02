contador_id_livro = 1
contador_id_membro = 1000

class Livro:
    def __init__(self, titulo:str, autor:str, livro_id:int):
        self.titulo = titulo
        self.autor = autor
        self.livro_id = livro_id
        self.status_disponivel = True

class Membro:
    def __init__(self, nome: str, membro_id:int):
        self.nome = nome
        self.membro_id = membro_id
        self.historico = []

class Biblioteca:
    def __init__(self):
        self.catalogo = []
        self.membros = []

    def adicionar_livro(self):
        global contador_id_livro

        titulo = str(input("Digite o titulo do livro: ")).upper().strip()
        autor = str(input("Digite o nome do autor: ")).upper().strip()
        # livro_id = int(input("Digite o ID do livro: "))

        livro = Livro(titulo=titulo, autor=autor, livro_id=contador_id_livro)
        contador_id_livro += 1

        self.catalogo.append(livro)

        return f"Livro adicionado com sucesso! ID livro criado: {contador_id_livro-1}"
                

    def adicionar_membro(self):
        global contador_id_membro
        nome_membro = str(input("Digite o nome do novo membro: ")).upper().strip()
        # membro_id = int(input("Crie o ID do usuário: "))

        membro = Membro(nome=nome_membro, membro_id=contador_id_membro)
        contador_id_membro += 1
        self.membros.append(membro)

        return f"Novo membro adicionado com sucesso! ID membro criado: {contador_id_membro-1}"
        

    def pesquisar_livro(self):
        livro_pesquisado = str(int("Digite o ID ou nome do livro que deseja pesquisar: "))
        for livro_da_vez in self.catalogo:
            if livro_da_vez.titulo == livro_pesquisado or livro_da_vez.livro_id == int(livro_pesquisado):
                print(f"""
                Informações do livro encontradas:
                Título: {livro_da_vez.titulo}
                Autor: {livro_da_vez.autor}
                Livro ID: {livro_da_vez.livro_id}
                Status disponível: {livro_da_vez.status_disponivel}
""")
            else:
                print("Livro não encontrado.")
            # else:
            #     print("O livro está indisponível no momento.")
    
    def pegar_livro_emprestado(self):
        membro_id = int(input("Digite o ID do membro que vai pegar o livro emprestado: "))
        for membro_atual in self.membros:
            if membro_atual.id == membro_id:
                livro_id = int(input(f"{membro_atual.nome}, digite o ID do livro que deseja emprestar: "))
                for livro_atual in self.catalogo:
                    if livro_atual.id == livro_id:
                        if livro_atual.status_disponivel:
                            livro_atual.status_disponivel == False
                            membro_atual.historico.append(livro_atual)
                            return "Livro emprestado com sucesso"
                        else:
                            return "Livro encontrado, porém já está emprestado."
            else:
                return "Desculpe, membro não encontrado."
        
    def devolver_livro(self):
        livro_devolvido = int(input("Digite a ID do livro que está devolvendo: "))
        for livro_em_devolucao in self.catalogo:
            if livro_em_devolucao.livro_id == livro_devolvido:
                livro_em_devolucao.status_disponivel = True

            return 

    def ver_historico(self):
        pass

biblioteca1 = Biblioteca()

while True:
    print("""
    MENU:
    1 - Adicionar livro
    2 - Adicionar membro
    3 - Pesquisar livro
    4 - Pegar livro emprestado
    5 - Devolver Livro
    6 - Ver histórico
    0 - Sair
    """)
    menu = int(input("Escolha sua opção: "))

    match menu:
        case 1:
            print(biblioteca1.adicionar_livro())
        case 2:
            print(biblioteca1.adicionar_membro())
        case 3:
            print(biblioteca1.pesquisar_livro())
        case 4:
            print(biblioteca1.pegar_livro_emprestado())
        case 5:
            print(biblioteca1.devolver_livro())
        case 6:
            print(biblioteca1.ver_historico())
        case 0:
            break
        case _:
            print("Você digitou uma opção inválida. Tente novamente.")