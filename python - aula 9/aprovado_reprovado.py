from tkinter import *

caixinha = Tk()
caixinha.title("Aprovado ou Reprovado?")
caixinha.geometry("300x200")
caixinha.configure(bg="#EADEDA")

def aprovacao():
    try:
        nota_portugues_valor = float(nota_portugues_input.get())
        nota_matematica_valor = float(nota_matematica_input.get())

        media = (nota_portugues_valor + nota_matematica_valor) / 2
        if media >= 7:
            resultado.configure(text="APROVADO", bg="green", fg="white")
        else:
            resultado.configure(text="REPROVADO", bg="red", fg="white")
    except ValueError:
        resultado.configure(text="Erro: Insira valores numéricos", bg="yellow", fg="black")
        return



nota_portugues = Label(text="Digite sua nota - PORTUGUÊS: ", fg="#2E294E", bg="#D90368")
nota_portugues.pack()

nota_portugues_input = Entry()
nota_portugues_input.pack()

nota_matematica = Label(text="Digite sua nota - MATEMÁTICA: ", fg="#2E294E", bg="#D90368")
nota_matematica.pack()

nota_matematica_input = Entry()
nota_matematica_input.pack()

botao = Button(caixinha, text="submeter", command=aprovacao)
botao.pack()

resultado = Label(text="RESULTADO", bg="#2E294E", fg="#EADEDA")
resultado.pack()

caixinha.mainloop()
