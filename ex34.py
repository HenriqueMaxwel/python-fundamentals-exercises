salario = float(input('Qual é o salário atual do funcionário? R$'))

if salario <= 1250:
    aumento = salario+(salario*0.15)
else:
    aumento = salario+(salario*0.10)

print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salario, aumento))