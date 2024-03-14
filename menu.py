import os
os.system('cls')

import math

continuar = 1

while continuar != 0:

    os.system('cls')

    print('''\n   <MENU>
                
        Opção 0 - Sair
        Opção 1 - O maior entre dois números
        Opção 2 - Com sua idade atual, você pode votar?
        Opção 3 - Acesso com senha
        Opção 4 - Venda de maças
        Opção 5 - Ordem crescente de 3 números
        Opção 6 - Seuu peso ideal
        Opção 7 - Poligonos regulares
        Opção 8 - Poligonos regulares (com verificação de lados)
        Opção 9 - Maior entre 3 números
        Opção 10 - Triangulo Equilátero, Isóscele ou Escaleno
        Opção 11 - Triangulo Retângulo, Obtusângulo ou Acutângulo
        ''')

    opcao = int(input('Digite a opção desejada: '))

    print('\n')

    match opcao:

        case 0:
            print('Programa encerrado')
            break
        case 1:
            n1 = int(input('Digite o primeiro numero: '))

            n2 = int(input('Digite o segundo numero: '))

            if n1 > n2:
                print(f'\n{n1} é maior que {n2}\n')
            else:
                print(f'\n{n2} é maior que {n1}\n')

        case 2:
            idade = int(input('Digite o ano que nasceu: '))

            if idade > 2008:
                print(f'\nvocê que tem {2024-idade} anos e não pode votar\n')
            else:
                print(f'\nVocê que tem {2024-idade} anos e pode votar\n')

        case 3:
            senha = 1234

            confirmacao_senha = int(input('Digite sua senha: '))

            if confirmacao_senha == senha:
                print('\nACESSO PERMITIDO\n')
            else:
                print('\nACESSO NEGADO\n')

        case 4:
            maca = 0.30

            qntd_maca = int(input('Digite a quantidade de maças compradas: '))

            if qntd_maca > 12:
                maca = 0.25
        
            print(f'\nvoce comprou {qntd_maca} maçãs e o valor foi {qntd_maca*maca}\n')

        case 5:
            n1 = int(input('Digite o primeiro numero: '))

            n2 = int(input('Digite o segundo numero: '))

            n3 = int(input('Digite o terceiro numero: '))

            if (n1 > n2 and n1 > n3) and n2 > n3:
                print(f'\n{n1} {n2} {n3}\n')

            elif (n1 > n2 and n1 > n3) and n3 > n2:
                print(f'\n{n1} {n3} {n2}\n')

            elif (n2 > n1 and n2 > n3) and n1 > n3:
                print(f'\n{n2} {n1} {n3}\n')

            elif (n2 > n1 and n2 > n3) and n3 > n1:
                print(f'\n{n2} {n3} {n1}\n')
        
            elif (n3 > n1 and n3 > n2) and n2 > n1:
                print(f'\n{n3} {n2} {n1}\n')
            else:
                print(f'\n{n3} {n1} {n2}\n')

        case 6:
            altura = float(input('Digite sua altura: '))
            peso = float(input('Digite seu peso: '))
            genero = int(input('1: Feminino 2: Masculino: '))
            peso_ideal = 0

            match genero:
                case 1:
                    peso_ideal = (62.1 * altura) - 44.7
                    print(f'\nSeu peso ideal é {peso_ideal}\n')
                case 2:
                    peso_ideal = (72.7 * altura) - 58
                    print(f'\nSeu peso ideal é {peso_ideal}\n')
                case _:
                    print('\nOpção invalida\n')

        case 7:
            ladosPolignono = int(input('Insira a quantidade de lados do poligono: '))

            areaPoligono = float(input('Digite a medida do lado em centimetros: '))

            area = 0

            if ladosPolignono == 3:

                area = (areaPoligono * areaPoligono) / 2
                print(f'\nSeu poligono é um triangulo e  o valor da area é {area}\n')

            elif ladosPolignono == 4:

                area = areaPoligono * areaPoligono
                print(f'\nSeu poligono é um quadrado e o valor da area é {area}\n')
            else:

                area = 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * areaPoligono **2
                print(f'\nSeu poligono é um pentagono e o valor da area é {area}\n')

        case 8:
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

        case 9:
            n1 = int(input('Digite o primeiro numero: '))

            n2 = int(input('Digite o segundo numero: '))

            n3 = int(input('Digite o terceiro numero: '))

            if n1 > n2 and n1 > n3:
                print(f'\n{n1} é o maior número\n')

            elif n2 > n1 and n2 > n3:
                print(f'\n{n2} é o maior número\n')

            elif n3 > n1 and n3 > n2:
                print(f'\n{n3} é o maior número\n')

        case 10:
            lado1 = int(input('Digite o primeiro lado: '))

            lado2 = int(input('Digite o segundo lado: '))

            lado3 = int(input('Digite o terceiro lado: '))

            if lado1 == lado2 and lado1 == lado3:
                print('\nTriangulo Equilátero\n')

            elif lado1 == lado2 or lado1 == lado3:
                print('\nTriangulo Isóscele\n')

            elif lado2 == lado1 or lado2 == lado3:
                print('\nTriangulo Isóscele\n')

            elif lado3 == lado1 or lado3 == lado2:
                print('\nTriangulo Isóscele\n')

            if lado1 != lado2 and lado1 != lado3:
                print('\nTriangulo Escaleno\n')

        case 11:
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

        case _:
            print('Opção invalida')
            
    continuar = int(input('Quer continuar?? [1] SIM [0] NÂO: '))

    if continuar == 0:
        print('\nPrograma encerrado')
        exit()
    elif continuar == 1:
        continue
    else:
        print('\nOpção invalida')
        exit()