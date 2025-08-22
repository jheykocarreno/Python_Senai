import random

numeros=[]
numSorteio=[]

def numJogador():
    print("Seleciona 6 numeros")
    
    
    i=0
    while i < 6:
        numeros.append(int(input(f"Numero {i+1}: ")))
        print(numeros)
        i+=1

    print(sorted(numeros))

def sorteio():
    numSorteio = list(range(1,61))
    sorteio = random.sample(numSorteio,6)
    print(sorteio)
    print(sorted(sorteio))

def comparar():
    comuns = list(set(numeros)&set(numSorteio))
    print(comuns)

numJogador()
sorteio()
comparar()