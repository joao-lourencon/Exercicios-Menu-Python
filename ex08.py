import os
os.system('cls')

import math

ladosPolignono = int(input('Insira a quantidade de lados do poligono: '))

areaPoligono = float(input('Digite a medida do lado em centimetros: '))

area = 0

print('\n')

if ladosPolignono < 3:
    print('Não é um poligono')

elif ladosPolignono > 5:
    print('Poligono não identificado')
    
elif ladosPolignono == 3:

    area = (areaPoligono * areaPoligono) / 2
    print(f'Seu poligono é um triangulo e  o valor da area é {area}')
elif ladosPolignono == 4:

    area = areaPoligono * areaPoligono
    print(f'Seu poligono é um quadrilátero e o valor da area é {area}')
else:

    area = 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * areaPoligono **2
    print(f'Seu poligono é um pentagono e o valor da area é {area}')