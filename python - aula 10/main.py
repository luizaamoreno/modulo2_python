from tkinter import *

janelinha = Tk()
janelinha.title("Revisão")
janelinha.geometry("350x350")

def saudacao():
    nome_digitado = nome_input.get()
    resposta.configure(text=f"Seja bem vindo {nome_digitado}")


nome_label = Label(text="Digite seu nome", bg="red", fg="white")
nome_label.pack()

nome_input = Entry()
nome_input.pack()

botao = Button(janelinha, text="Enviar", command=saudacao)
botao.pack()

resposta = Label(text="")
resposta.pack()


janelinha.mainloop()