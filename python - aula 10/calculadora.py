from tkinter import *

calculadora = Tk()
calculadora.title("Calculator")
calculadora.geometry("350x600")

B7 = Button(calculadora, text="7", width=10, height=5, pady=10)
B7.grid(row=2, column=0)

B8 = Button(calculadora, text="8", width=10, height=5, pady=10)
B8.grid(row=2, column=1)

B9 = Button(calculadora, text="9", width=10, height=5, pady=10)
B9.grid(row=2, column=2)

B4 = Button(calculadora, text="4", width=10, height=5, pady=10)
B4.grid(row=3, column=0)

B5 = Button(calculadora, text="5", width=10, height=5, pady=10)
B5.grid(row=3, column=1)

B6 = Button(calculadora, text="6", width=10, height=5, pady=10)
B6.grid(row=3, column=2)

B1 = Button(calculadora, text="1", width=10, height=5, pady=10)
B1.grid(row=4, column=0)

B2 = Button(calculadora, text="2", width=10, height=5, pady=10)
B2.grid(row=4, column=1)

B3 = Button(calculadora, text="3", width=10, height=5, pady=10)
B3.grid(row=4, column=2)

B0 = Button(calculadora, text="0", width=20, height=5, pady=10)
B0.grid(row=5, column=2)

calculadora.mainloop()