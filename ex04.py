import os
os.system('cls')

maca = 0.30

qntd_maca = int(input('Digite a quantidade de maças compradas: '))

if qntd_maca > 12:
    maca = 0.25
    
print(f'voce comprou {qntd_maca} maçãs e o valor foi {qntd_maca*maca}')
