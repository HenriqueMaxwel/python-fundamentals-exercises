#Exercise 040(School Point Average)
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = float((n1+n2)/2)

if media >= 7:
    print('A sua média foi {:.2f}, parabens, você foi \033[4;32; mAPROVADO!\033[m'.format(media))
elif 5 <= media < 7:
    print('A sua média foi {:.2f}, você está de \033[4;33; mRECUPERAÇÃO!\033[m'.format(media))
elif media < 5:
    print('A sua média foi {:.2f}, você foi \033[4;31; mREPROVADO!\033[m'.format(media))
