#Exercise 044(Payment Manager)

valor = float(input('Digite o valor do produto: R$'))
pagamento = int(input('''
1- À vista dinheiro/cheque 
2- À vista no cartão 
3- 2x no cartão 
4- 3x ou mais no cartão 
Digite a forma de pagamento: '''))


print('-'*30)
print('Valor do produto: R${:.2f}'.format(valor))

if pagamento == 1:
    preco = valor - (valor * 0.10)
elif pagamento == 2:
    preco = valor - (valor * 0.05)
elif pagamento == 3:
    preco = valor
    parcela = preco/2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif pagamento == 4:
    preco = valor + (valor*0.20)
    totalparc = int(input('Quantas parcelas? '))
    parcela = preco/totalparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totalparc, parcela))
else:
    preco = None
    print('Opção de pagamento inválida, tente novamente!')


print('Valor do produto: R${:.2f}'.format(valor))
print('Sua compra tem o valor à ser pago de: R${:.2f}'.format(preco))
