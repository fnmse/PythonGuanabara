from random import randint
from time import sleep
n=randint(0,5)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('--'*10)
r=int(input('Qual número eu pensei? '))
print('Processando...')
sleep(3)
print('\033[33mParabéns! vc venceu\033[m'if r==n else '\033[31mPerdeu! Eu pensei no número {}\033[m'.format(n))
