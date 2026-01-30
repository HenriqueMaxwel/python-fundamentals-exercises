#Exercise 043(Body Mass Index)
altura = float(input('Digite sua altura em metros: '))
peso = float(input('Digite seu peso em KG: '))
imc = peso/(altura**2)

if imc < 18.5:
    print('Altura: {} \nPeso: {} \nIMC: {:.2f} \nVocê está ABAIXO do peso.'.format(altura,peso,imc))
elif imc <= 25:
    print('Altura: {} \nPeso: {} \nIMC: {:.2f} \nVocê está com o peso IDEAL.'.format(altura,peso,imc))
elif imc <= 30:
    print('Altura: {} \nPeso: {} \nIMC: {:.2f} \nVocê está ACIMA do peso.'.format(altura, peso, imc))
elif imc <= 40:
    print('Altura: {} \nPeso: {} \nIMC: {:.2f} \nVocê está OBESO.'.format(altura, peso, imc))
else:
    print('Altura: {} \nPeso: {} \nIMC: {:.2f} \nVocê está no estado de OBESIDADE MÓRBIDA.'.format(altura, peso, imc))
