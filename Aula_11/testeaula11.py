with open("teste.txt", "w") as t:
    t.write("Linha 1 criada com modo W\n")
    t.write("Linha 2 criada com modo W\n")
    # /n cria uma quebra na lina após sua chamada

with open("teste.txt", "a") as t:
    t.write("Batatinha quando nasce\n")
    t.write("Batatinha quando nasce\n Espalha a rama pelo chão\n Menininha quando dorme\n Põe a mão no coração.\n")
    #Lendo para verificar
with open("teste.txt", "r") as t:
    print("Conteudo após modo w:\n", t.read())