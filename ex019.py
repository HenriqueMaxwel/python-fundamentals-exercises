"""import random

nome0 = input('Digite o primeiro nome: ')
nome1 = input('Digite o segundo nome: ')
nome2 = input('Digite o terceiro nome: ')
nome3 = input('Digite o quarto nome: ')
nome4 = input('Digite o quinto nome: ')

sorteio = random.choice(nome0)
print('A palavra escolhida foi {}'.format(sorteio)) """

#RESOLUÇÃO

import random

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
n5 = str(input('Quinto aluno:'))
lista = [n1, n2, n3, n4]

sorteio = random.choice(lista)
print('O nome escolhido foi {}'.format(sorteio))