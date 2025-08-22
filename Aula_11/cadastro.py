import csv
import os

#nome do arquivo
arquivo="cadastro.csv"

#verifica se o arquivo existe. Se não, cria com cabecalho
if not os.path.exists(arquivo):
    with open(arquivo, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Nome", "Telefone", "Email"])

#Função para cadastrar uma pessoa
def cadastrar():
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")
    with open(arquivo, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([nome, telefone, email]),
    print("Cadastro realizado com sucesso\n")

#Funcão para listar todos os cadastros
def listar():
    print("\nLista de cadastros: ")
    with open(arquivo, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for linha in reader:
            print(" | ".join(linha))
    print()

#Menu simples
while True:
    print("1 - Cadastrar pessoa")
    print("2 - Listar cadastros")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        print("Saindo...")
        break
    else:
        print("Opcao invalida, tente novamente.\n")