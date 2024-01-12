class Tamagotchi:
    def __init__(self, nome, especie, energia):
        self.nome = nome
        self.especie = especie
        self.energia = energia

    def brincar(self):
        if self.energia >= 5 and self.energia <= 100:
            self.energia = self.energia - 5
            return self.energia
        else:
            print("Passou da hora de comeeeeer!")
    
    def comer(self):
        if self.energia < 100:
            self.energia = self.energia + 5
        elif self.energia >= 100:
            print("Já comeu demais, pode ir brincar!")
    
    def ver_informacoes(self):
        return f"""
        Nome: {self.nome}
        Espécie: {self.especie}
        Energia atual: {self.energia}
        """



tamagotchi1 = Tamagotchi(nome = "Lion", especie = "terrestre", energia=100)

while True:
    menu = int(input("""
    ** MENU **:
    1 - Brincar
    2 - Comer
    3 - Condição atual
    0 - Sair

    Escolha uma opção: 
    """))

    match menu:
        case 1:
            tamagotchi1.brincar()
        case 2:
            tamagotchi1.comer()
        case 3:
            print(tamagotchi1.ver_informacoes())
        case 0:
            break
        case _:
            print("Opção inválida.")

    print(f"Energia atual: {tamagotchi1.energia}")
    

