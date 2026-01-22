nome = str(input('Digite seu nome completo: '))
dividido = nome.split()

print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome ao todo tem {}'.format(len("".join(nome.split()))) + ' letras')
print('Seu primeiro nome é {}'.format(dividido[0]) + ' e ele tem {}'.format(len(dividido[0])) + ' letras')