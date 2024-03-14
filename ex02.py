import os
os.system('cls')

idade = int(input('Digite o ano que nasceu: '))

if idade > 2008:
    print(f'você que tem {2024-idade} anos não pode votar')
else:
    print(f'Você que tem {2024-idade} anos pode votar')