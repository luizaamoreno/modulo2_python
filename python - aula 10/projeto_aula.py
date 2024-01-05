#FAÇA UMA INTERFACE QUE PEDE PARA O USUÁRIO DIGITAR 3 NOTAS E UM BOTÃO QUE AO SER CLICADO MOSTRA NA TELA UMA MENSAGEM "APROVADO" SE A MÉDIA FOR
#MAIOR OU IGUAL A 7 COM A COR VERDE, "REPROVADO" SE A MÉDIA FOR MENOR DO QUE 7 COM A COR DE FUNDO VERMELHO E "APROVADO COM DISTINÇÃO" SE A MÉDIA FOR IGUAL A 10 COM A COR DE FUNDO AZUL.

from tkinter import *

caixinha = Tk()
caixinha.title("Aprovado ou Reprovado?")
caixinha.geometry("300x200")
caixinha.configure(bg="#EADEDA")

def aprovacao():
    try:
        nota_prova1_valor = float(nota_prova1_input.get())
        nota_prova2_valor = float(nota_prova2_input.get())
        nota_prova3_valor = float(nota_prova3_input.get())

        media = (nota_prova1_valor + nota_prova2_valor + nota_prova3_valor) / 3
        if media == 10:
            resultado.configure(text="APROVADO COM DISTINÇÃO", bg="blue", fg="white")
        elif media >= 7 and media < 10:
            resultado.configure(text="APROVADO", bg="green", fg="white")
        else:
            resultado.configure(text="REPROVADO", bg="red", fg="white")
    except ValueError:
        resultado.configure(text="Erro: Insira valores numéricos", bg="yellow", fg="black")
        return

nota_prova1 = Label(text="Digite sua nota - PROVA 1: ", fg="#2E294E", bg="#D90368")
nota_prova1.pack()

nota_prova1_input = Entry()
nota_prova1_input.pack()

nota_prova2 = Label(text="Digite sua nota - PROVA 2: ", fg="#2E294E", bg="#D90368")
nota_prova2.pack()

nota_prova2_input = Entry()
nota_prova2_input.pack()

nota_prova3 = Label(text="Digite sua nota - PROVA 3: ", fg="#2E294E", bg="#D90368")
nota_prova3.pack()

nota_prova3_input = Entry()
nota_prova3_input.pack()

botao = Button(caixinha, text="submeter", command=aprovacao)
botao.pack()

resultado = Label(text="RESULTADO", bg="#2E294E", fg="#EADEDA")
resultado.pack()

caixinha.mainloop()