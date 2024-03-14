import os
os.system('cls')


n1 = int(input('Digite o primeiro numero: '))

n2 = int(input('Digite o segundo numero: '))

if n1 > n2:
    print(f'{n1} é maior que {n2}')
else:
    print(f'{n2} é maior que {n1}')