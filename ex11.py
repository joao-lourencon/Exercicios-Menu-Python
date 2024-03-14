import os
os.system('cls')

angulo1 = int(input('Digite o primeiro angulo: '))

angulo2 = int(input('Digite o segundo angulo: '))

angulo3 = int(input('Digite o terceiro angulo: '))

print('\n')

if (angulo1 or angulo2 or angulo3) == 90:
    print(f'Por possuir um angulo reto (de 90 graus), é um triangulo Retângulo')

elif (angulo1 or angulo2 or angulo3) > 90:
    print('Por só possuir um angulo obtuso (maior que 90 graus), é um triangulo Obtusângulo')

elif (angulo1 or angulo2 or angulo3) < 90:
    print('Por só possuir angulos agudos (menores que 90 graus), é um triangulo Acutângulo')
