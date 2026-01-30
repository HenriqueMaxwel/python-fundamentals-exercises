#Exercise 041(Classifying Athletes)
from datetime import date
print('-='*20)
print('\033[4;36; mConfederação Nacional de Natação\033[m')
print('-='*20)

data = int(input('Digite o seu ano de nascimento: '))
idade = date.today().year - data

if idade <= 9:
    print('Voce tem {} anos, sua categoria é MIRIM'.format(idade))
elif idade <= 14:
    print('Voce tem {} anos, sua categoria é INFANTIL'.format(idade))
elif idade <= 19:
    print('Voce tem {} anos, sua categoria é JÚNIOR'.format(idade))
elif idade <= 25:
    print('Voce tem {} anos, sua categoria é SÊNIOR'.format(idade))
elif idade > 25:
    print('Voce tem {} anos, sua categoria é MASTER'.format(idade))