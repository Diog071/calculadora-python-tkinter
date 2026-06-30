import tkinter as tk

def clicar(botao):
    atual = entrada.get()

    if botao == "C":
        entrada.delete(0, tk.END)

    elif botao == "=":
        try:
            resultado = eval(atual)
            entrada.delete(0, tk.END)
            entrada.insert(0, str(resultado))
        except:
            entrada.delete(0, tk.END)
            entrada.insert(0, "Erro")

    else:
        entrada.insert(tk.END, botao)


# Janela principal
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x425")
janela.resizable(False, False)

# Campo de entrada
entrada = tk.Entry(janela, font=("Arial", 20), bd=10, justify="right")
entrada.pack(fill="both", padx=10, pady=10)

# Botões
botoes = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C"
]

frame = tk.Frame(janela)
frame.pack()

linha = 0
coluna = 0

for botao in botoes:
    comando = lambda x=botao: clicar(x)
    tk.Button(
        frame,
        text=botao,
        width=5,
        height=2,
        font=("Arial", 14),
        command=comando
    ).grid(row=linha, column=coluna, padx=5, pady=5)

    coluna += 1
    if coluna > 3:
        coluna = 0
        linha += 1

janela.mainloop()
