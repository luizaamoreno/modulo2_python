from tkinter import *

caixinha = Tk()
caixinha.title("Aula 1 Tkinter")
caixinha.geometry("400x400")
caixinha.configure(bg="#EADEDA")

def mostrar_nome():
    print(nome_input.get())


nome = Label(text="Digite seu nome: ", fg="#2E294E", bg="#D90368")
nome.pack()

nome_input = Entry()
nome_input.pack()

botao = Button(caixinha, text="enviar", command=mostrar_nome)
botao.pack()

caixinha.mainloop()