import tkinter as tk
from tkinter import messagebox

def calcular():
    v1 = float(alcool.get())
    v2 = float(gasolina.get())

    res = v1/v2

    if(res>=0.7):
        resultado.set("Gasolina")
    else:
        resultado.set("Alcool")

def limpar():
    v1 = alcool.delete(0, tk.END)
    v2 = gasolina.delete(0, tk.END)
    resultado.set("")

posto = tk.Tk()
posto.title("Melhor Combustivel")
posto.geometry("280x200")

tk.Label(posto, text = "ALCOOL: ").grid(row=0, column=0, padx=5, pady=5, )
alcool = tk.Entry(posto)
alcool.grid(row=0, column=1, padx=5, pady=5)

tk.Label(posto, text="GASOLINA: ").grid(row=1, column=0, padx=5, pady=5)
gasolina = tk.Entry(posto)
gasolina.grid(row=1, column=1, padx=5, pady=5)

botao_calc = tk.Button(posto, text="Calcular", width=10, command=calcular)
botao_calc.grid(row=2, column=1, padx=5, pady=5)
botao_limp = tk.Button(posto, text="Limpar", width=10, command=limpar)
botao_limp.grid(row=3, column=1, padx=5, pady=5)

resultado = tk.StringVar()
tk.Label(posto, text="Melhor opcão: ").grid(row=4, column=0, padx=5, pady=5)
tk.Label(posto, textvariable=resultado, font=("Arial, 14")).grid(row=4, column=1, padx=5, pady=5)

posto.mainloop()