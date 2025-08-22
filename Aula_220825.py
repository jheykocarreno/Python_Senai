import random

numero = random.randint(1,60)
print(numero)

decimal = random.random()
print(decimal)

cores=['vermelho','azul','verde']
cor = random.choice(cores)
print(cor)

#import random
numeros = list(range(1,61))
sorteio = random.sample(numeros,6)
print(sorteio)

cartas = ['A', '2', '3', '5', '4']
random.shuffle(cartas)
print(cartas)


#blibliotecas para utilizar. 
#debemos instalar despues de python y vscode.
#estas lineas de codigo, lo ejecutamos en cmd o powershell
#pip install requests
#pip install numpy
#pip pandas