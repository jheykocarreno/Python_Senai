import tkinter as tk
from tkinter import messagebox
app = tk.Tk()
app.title("Minha Janela APP")
app.geometry("600x300")

label = tk.Label(app, text="Ola, Tkinter!", font=("Arial, 14"))
label.pack()
def clique():
    nome = entrada.get()
    messagebox.showinfo("Mensagem", nome+" você clicou no botão")
botao = tk.Button(app, text="Clique aqui", command = clique)
botao.pack()
entrada = tk.Entry(app)
entrada.pack()
app.mainloop()