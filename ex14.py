import os
os.system('cls')

salaAula = [10]

i2 = 0
i = 0
soma = 0

for salaAula in range(10):
    i += 1

    print("\nAluno", i)

    while True:
        nota1 = float(input('Nota 1: '))
        if 0 <= nota1 <= 10:
            break
        else:
            print('Nota inválida. Por favor, insira novamente: ')
            
    while True:
        nota2 = float(input('Nota 2: '))
        if 0 <= nota2 <= 10:
            break
        else:
            print('Nota inválida. Por favor, insira novamente: ')

    while True:
        nota3 = float(input('Nota 3: '))
        if 0 <= nota3 <= 10:
            break
        else:
            print('Nota inválida. Por favor, insira novamente: ')

if nota1 < nota2 and nota1 < nota3:
    media = (nota2 + nota3) / 2
  
elif nota2 < nota1 and nota2 < nota3:
    media = (nota1 + nota3) / 2

elif nota3 < nota1 and nota3 < nota2:
    media = (nota1 + nota2) / 2

print('\n')

for soma in range(10):
    i2 += 1
    print(f'Aluno {i2}: media {media} \n')