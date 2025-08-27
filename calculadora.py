import tkinter as tk
#area das funcoes:
def soma():
    try:
        v1 = float(entrada1.get())
        v2 = float(entrada2.get())
        resultado.set(v1+v2)
    except ValueError:
        resultado.set("Algun valor esta incorreto")

def subi():
    v1 = float(entrada1.get())
    v2 = float(entrada2.get())
    resultado.set(v1-v2)

def mult():
    v1 = float(entrada1.get())
    v2 = float(entrada2.get())
    resultado.set(v1*v2)

def divi():
    v1 = float(entrada1.get())
    v2 = float(entrada2.get())
    if (v2==0):
        resultado.set("Error")
    else:
        resultado.set(v1/v2)

def pote():
    v1 = float(entrada1.get())
    v2 = float(entrada2.get())
    resultado.set(v1**v2)

def limp():
    v1 = entrada1.delete(0, tk.END)
    v2 = entrada2.delete(0, tk.END)
    resultado.set("")

#area do app
calc = tk.Tk()
calc.title("Calculadora Simples")
calc.geometry("320x320")

#Rotulos e caixas de texto
tk.Label(calc, text = "Valor 1: ").grid(row=0, column=0, padx=5, pady=5)
entrada1 = tk.Entry(calc)
entrada1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(calc, text="Valor 2: ").grid(row=1, column=0, padx=5, pady=5)
entrada2 = tk.Entry(calc)
entrada2.grid(row=1, column=1, padx=5, pady=5)

#Label de resultado
resultado = tk.StringVar()
tk.Label(calc, text="Resultado: ").grid(row=2, column=0, padx=5, pady=5)
tk.Label(calc, textvariable=resultado).grid(row=2, column=1, padx=5, pady=5)

#Botoes criados individualmente
botao_soma = tk.Button(calc, text="+", width=5, command=soma)
botao_soma.grid(row=3, column=0, padx=5, pady=5)
botao_soma = tk.Button(calc, text="-", width=5, command=subi)
botao_soma.grid(row=3, column=1, padx=5, pady=5)
botao_soma = tk.Button(calc, text="x", width=5, command=mult)
botao_soma.grid(row=3, column=2, padx=5, pady=5)
botao_soma = tk.Button(calc, text="/", width=5, command=divi)
botao_soma.grid(row=4, column=0, padx=5, pady=5)
botao_soma = tk.Button(calc, text="**", width=5, command=pote)
botao_soma.grid(row=4, column=1, padx=5, pady=5)
botao_soma = tk.Button(calc, text="C", width=5, command=limp)
botao_soma.grid(row=4, column=2, padx=5, pady=5)
calc.mainloop()
