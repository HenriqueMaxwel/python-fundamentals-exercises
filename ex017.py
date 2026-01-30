import math
from math import hypot

# c² = a² + b²
'''cat_op = float(input('Qual a medida do cateto oposto? '))
cat_ad = float(input('Qual a medida do cateto adjacente? '))
hipot = (cat_op**2) + (cat_ad**2)

print('O comprimento da hipotenusa é {:.3f}!'.format(math.sqrt(hipot)))'''

cat_op = float(input('Qual a medida do cateto oposto? '))
cat_ad = float(input('Qual a medida do cateto adjacente?'))
hipot = math.hypot(cat_op, cat_ad)

print('O comprimento da hipotenusa é {:.2f}'.format(hipot))