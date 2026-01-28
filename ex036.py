#Exercise 036 (Bank Loan)
valor = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
financiamento = int(input('Quantos anos de financiamento: '))

tempo = financiamento * 12
prestacao = valor/tempo
porcento_salario = salario * 0.30

print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(valor, financiamento, prestacao))

if prestacao > porcento_salario:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo CONCEDIDO!')