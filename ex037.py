#Exercise 037 (Number Base Converter)
num = int(input('Digite um número inteiro: '))
conversao = input('1-Binário \n2-Octal \n3-Hexadecimal \nEscolha a base de conversão: ')
format_conversao = conversao.upper()

print('O número {} no formato escolhido ({}):'.format(num, conversao))

if format_conversao == '1' or format_conversao == 'BINÁRIO' or format_conversao == 'BINARIO':
    print(bin(num)[2:])
elif format_conversao == '2' or format_conversao == 'OCTAL':
    print(oct(num)[2:])
elif format_conversao == '3' or format_conversao == 'HEXADECIMAL':
    print(hex(num)[2:])
else:
    print('Opção {} inválida!.'.format(format_conversao))