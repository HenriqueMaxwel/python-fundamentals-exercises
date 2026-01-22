frase = str(input('Digite uma frase: ')).strip().upper()
primeira = frase.find('A')
ultima = frase.rfind('A')

print('A letra "A" aparace {} vezes na frase'.format(frase.upper().count('A')))
print('A primeira letra "A" aparaceu na posição {}' .format(primeira + 1))
print('A ultima letra "A" aparece na posição {}'.format(ultima + 1))