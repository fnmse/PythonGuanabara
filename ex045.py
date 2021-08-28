from random import randint
from time import sleep
iten=('Pedra', 'Papel', 'Tesoura')
pc=randint(0,2)
print(''' As opções são:
[0] Pedra
[1] Papel
[2] Tesoura
''')
j=int(input('Qual é a sua jogada?'))
print('\033[33mPedra\033[m')
sleep(1)
print('\033[33mPapel\033[m')
sleep(1)
print('\033[33mTesoura\033[m')
sleep(1)
print('='*20)
print('Computador jogou {}'.format(iten[pc]))
print(' Jogador jogou {}'.format(iten[j]))
print('='*20)
if pc==0:
    if j==0:
        print('EMPATOU')
    elif j==1:
        print('JOGADOR VENCEU')
    elif j==2:
        print('Computador Venceu!')
    else:
        print('Jogada inválida')
elif pc==1: #computador jogou papel
    if j==0:
        print('Computador Venceu')
    elif j==1:
        print('Empatou')
    elif j==2:
        print('Jogador Venceu')

    else:
        print('Jogada inválida')

elif pc==2:# computador jogou tesoura
    if j == 0:
        print('Jogador venceu')

    elif j == 1:
        print('Computador venceu')

    elif j == 2:
        print('Empatou')

    else:
        print('Jogada inválida')






