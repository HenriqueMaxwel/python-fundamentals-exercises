n = int(input('Informe um número: '))
num = str(n)

print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(num[3:]))
print('Dezena: {}'.format(num[2:3]))
print('Centena: {}'.format(num[1:2]))
print('Milhar: {}'.format(num[0:1]))
