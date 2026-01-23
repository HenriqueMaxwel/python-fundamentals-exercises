velocidade = int(input('Qual a velocidade na qual voce estava dirigindo? '))
multa = (velocidade - 80) * 7

if velocidade > 80:
    print('MULTADO! Você excedeu o limite de velocidade que é de 80Km/h')
    print('Voce deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia, dirija com segurança!')
#exercicio