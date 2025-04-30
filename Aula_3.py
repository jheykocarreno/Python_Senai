print('SISTEMA DE NOTAS')

nome1 = input('Digite o nome do aluno 1: ')
nome2 = input('Digite o nome do aluno 2: ')
nome3 = input('Digite o nome do aluno 3: ')

print('Notas aluno', nome1)
nota1a = float(input('Nota1: '))
nota2a = float(input('Nota2: '))
nota3a = float(input('Nota3: '))
               
media1 = (nota1a + nota2a + nota3a) / 3
print('Aluno ', nome1, ' media ', media1)
      
Apro1 = media1 >= 7
Apro2 = media1 >= 5 and media1 < 7
Apro3 = media1 < 5

print(f'''
Aluno {nome1}:
Aprovado - {Apro1}
Recuperação - {Apro2}
Reprovado - {Apro3}
''')

print('Notas aluno', nome2)
nota1b = float(input('Nota1: '))
nota2b = float(input('Nota2: '))
nota3b = float(input('Nota3: '))

media2 = (nota1b + nota2b + nota3b) / 3
print('Aluno ', nome2, ' media ', media2)

Apro1 = media2 >= 7
Apro2 = media2 >= 5 and media2 < 7
Apro3 = media2 < 5

print(f'''
Aluno {nome2}:
Aprovado - {Apro1}
Recuperação - {Apro2}
Reprovado - {Apro3}
''')

print('Notas aluno', nome3)
nota1c = float(input('Nota1: '))
nota2c = float(input('Nota2: '))
nota3c = float(input('Nota3: '))

media3 = (nota1c + nota2c + nota3c) / 3
print('Aluno ', nome3, ' media ', media3)
      
Apro1 = media3 >= 7
Apro2 = media3 >= 5 and media3 < 7
Apro3 = media3 < 5

print(f'''
Aluno {nome3}:
Aprovado - {Apro1}
Recuperação - {Apro2}
Reprovado - {Apro3}
''')