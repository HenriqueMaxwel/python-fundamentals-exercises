#Exercise 044(Payment Manager)

valor = float(input('Digite o valor do produto: R$'))
pagamento = int(input('1- À vista dinheiro/cheque \n2- À vista no cartão \n3- 2x no cartão \n4- 3x ou mais no cartão \nDigite a forma de pagamento: '))
dinheiro = valor - (valor*0.10)
cartao = valor - (valor*0.05)
dividido3x = valor + (valor*0.20)

print('-'*30)
print('Valor do produto: R${}'.format(valor))
if pagamento == 1:
    print('Valor à ser pago: R${}'.format(dinheiro))
elif pagamento == 2:
    print('Valor à ser pago: R${}'.format(cartao))
elif pagamento == 3:
    print('Valor à ser pago: R${}'.format(valor))
elif pagamento == 4:
    print('Valor à ser pago: R${}'.format(dividido3x))
else:
    print('Opção de pagamento inválida, tente novamente!')