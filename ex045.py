#Exercise 045(GAME: Rock, Paper, Scissors)
import random
from time import sleep

print('-='*20)
print('PEDRA PAPEL OU TESOURA')
print('-='*20)

escolha = str(input('Faça sua escolha: ')).upper().strip()
lista = ['PEDRA', 'PAPEL', 'TESOURA']
computador = random.choice(lista)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
sleep(1)

print('='*35)
print('Voce escolheu {}'.format(escolha))
print('Computador escolheu {}'.format(computador))
print('='*35)

if escolha == computador:
    print('EMPATE!')
elif escolha == 'PEDRA' and computador == 'TESOURA':
    print('VOCÊ GANHOU!')
elif escolha == 'PAPEL' and computador == 'PEDRA':
    print('VOCÊ GANHOU!')
elif escolha == 'TESOURA' and computador == 'PAPEL':
    print('VOCÊ GANHOU!')
elif escolha in lista:
    print('VOCÊ PERDEU!')
else:
    print('escolha inválida!')