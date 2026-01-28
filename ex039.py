#Exercise 039 (Military Service)
from datetime import date
print('=-'*20)
print('\033[1;32; mSERVIÇO MILITAR\033[m')
print('=-'*20)

nasc = int(input('Digite seu ano de nascimento: '))
ano = date.today().year
rest = (ano-nasc)

if rest < 18:
    print('Faltam {} anos, para voce poder se alistar!'.format(18-rest))
elif rest == 18:
    print('Você esta com {} anos, a idade exata para se alistar!'.format(rest))
elif rest > 18:
    print('O ano de seu alistamento foi há {} anos atrás!'.format(rest-18))
