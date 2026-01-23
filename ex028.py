import random
from time import sleep
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
num = int(input('Em que número pensei? '))
print('PROCESSANDO...')
sleep(2)
comp_num = random.randint(0,5)
if num == comp_num:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}!'.format(comp_num, num))
#exercicio