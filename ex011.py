#Formula de área = altura * largura

weight = float(input('Qual a lagura da parede? '))
height = float(input('Qual a altura da parede? '))
area = (weight * height)

print('A area de sua parede é: {}m² \n Será nescessário para pintar a parede: {}L'.format(area, area/2))
