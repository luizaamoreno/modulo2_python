from tkinter import *
from datetime import datetime

caixinha = Tk()
caixinha.title("Maior de Idade?")
caixinha.geometry("200x200")
caixinha.configure(bg="#EADEDA")

def maioridade():
    ano_atual = datetime.now().year
    idade = ano_atual - int(ano_nascimento_input.get())
    if idade >= 18:
        resultado.configure(text="Resultado: Maior de Idade.")
    else:
        resultado.configure(text="Resultado: Menor de Idade.")

ano_nascimento = Label(text="Digite seu ano de nascimento: ", fg="#2E294E", bg="#D90368")
ano_nascimento.pack()

ano_nascimento_input = Entry()
ano_nascimento_input.pack()

botao = Button(caixinha, text="enviar", command=maioridade)
botao.pack()

resultado = Label(text="Resposta: ", bg="#2E294E", fg="#EADEDA")
resultado.pack()

caixinha.mainloop()