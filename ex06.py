import os
os.system('cls')

altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
genero = int(input('1: Feminino 2: Masculino: '))
peso_ideal = 0

match genero:
    case 1:
        peso_ideal = (62.1 * altura) - 44.7
        print(f'Seu peso ideal é {peso_ideal}')
    case 2:
        peso_ideal = (72.7 * altura) - 58
        print(f'Seu peso ideal é {peso_ideal}')
    case _:
        print('Opção invalida')