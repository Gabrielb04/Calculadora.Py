import tkinter as tk
from tkinter import messagebox

def adicionar_numero(numero):
    entrada_texto.insert(tk.END, numero)

def adicionar_operacao(operacao):
    entrada_texto.insert(tk.END, operacao)

def calcular():
    expressao = entrada_texto.get()
    try:
        resultado = eval(expressao)
        limpar()
        entrada_texto.insert(tk.END, str(resultado))
    except Exception as e:
        messagebox.showerror("Erro", f"Erro na expressão: {e}")

def limpar():
    entrada_texto.delete(0, tk.END)

root = tk.Tk()
root.title("Calculadora")
root.configure(bg="#000000")  # Definindo o fundo preto

entrada_texto = tk.Entry(root, font=("Arial", 18), justify="right", bg="#111111", fg="#8a2be2", insertbackground="#8a2be2")  # Definindo cores do Entry
entrada_texto.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="we")

botoes = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for texto, linha, coluna in botoes:
    if texto == "=":
        botao = tk.Button(root, text=texto, font=("Arial", 14), bg="#333333", fg="white", command=calcular)  # Definindo cores do botão
    elif texto == "C":
        botao = tk.Button(root, text=texto, font=("Arial", 14), bg="#333333", fg="white", command=limpar)  # Definindo cores do botão
    else:
        botao = tk.Button(root, text=texto, font=("Arial", 14), bg="#333333", fg="#8a2be2", command=lambda t=texto: adicionar_numero(t))  # Definindo cores do botão
    botao.grid(row=linha, column=coluna, padx=5, pady=5, sticky="we")

root.mainloop()
