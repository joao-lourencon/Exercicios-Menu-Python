import os
os.system('cls')

senha = 1234

input_senha = int(input('Digite sua senha: '))

if input_senha == senha:
    print('ACESSO PERMITIDO')
else:
    print('ACESSO NEGADO')

