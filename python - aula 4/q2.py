def contar_letra(caracters):
    contador_de_letra = 0
    contador_de_espacos = 0
    contador_de_pontuacao = 0

    if " " in caracters:
        for letra in caracters:
            if letra == " ":
                contador_de_espacos += 1
            elif letra.lower() in "abcdefghijklmnopqrstuvwxyz":
                contador_de_letra += 1
            elif letra in ".,;:?!@#$%¨&*-~^><\/+-":
                contador_de_pontuacao += 1
        return f"A frase tem {contador_de_letra} de caracteres, tem {contador_de_espacos} de espaços e {contador_de_pontuacao} de pontuação."
    else:
        return len(caracters)


palavra = str(input("Digite um texto ou uma palavra: ")).strip()

print(contar_letra(palavra))