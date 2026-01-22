dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
aluguel = 60 * dias
rodado = 0.15 * km
valor = aluguel + rodado

print('O total a pagar é de R${}'.format(valor))