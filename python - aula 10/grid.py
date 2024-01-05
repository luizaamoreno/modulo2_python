from tkinter import *

janela = Tk()
janela.title("Aprendendo grid")
janela.geometry("350x300")

nome_label = Label(text="Digite seu nome: ")
nome_label.grid(row=0, column=0, padx=30, pady=10)

nome_input = Entry()
nome_input.grid(row=0, column=1, padx=30, pady=10)

idade_label = Label(text = "Digite sua idade: ")
idade_label.grid(row=1, column=0)

idade_input = Entry()
idade_input.grid(row=1, column=1)

botao = Button(janela, text="Enviar", width=25, pady=10)
botao.grid(row=2, column=0, columnspan=2)

janela.mainloop()