"""from math import sin, cos, tan, ceil

num = int(input('Digite o ângulo que voce deseja: '))

seno = sin(num)
cosseno = cos(num)
tangente = tan(num)

result = print('O ângulo de {} tem o SENO de {}\n O ângulo de {} tem o COSSENO de {}\n O ângulo de {} tem o TANGENTE de {}'.format(num, ceil(seno), num, ceil(cosseno), num, ceil(tangente)))"""

#RESOLUÇÃO

import math
an = float(input('Digite o ângulo que voce deseja: '))
seno = math.sin(math.radians(an))
print('O ângulo de {} tem o SENO de {:.2f}'.format(an, seno))
cosseno = math.cos(math.radians(an))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(an, cosseno))
tangente = math.tan(math.radians(an))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(an, tangente))