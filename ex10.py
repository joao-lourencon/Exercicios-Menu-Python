import os
os.system('cls')

lado1 = int(input('Digite o primeiro lado: '))

lado2 = int(input('Digite o segundo lado: '))

lado3 = int(input('Digite o terceiro lado: '))

if lado1 == lado2 and lado1 == lado3:
    print('Triangulo Equilátero')

elif lado1 == lado2 or lado1 == lado3:
    print('Triangulo Isóscele')

elif lado2 == lado1 or lado2 == lado3:
    print('Triangulo Isóscele')

elif lado3 == lado1 or lado3 == lado2:
    print('Triangulo Isóscele')

if lado1 != lado2 and lado1 != lado3:
    print('Triangulo Escaleno')
