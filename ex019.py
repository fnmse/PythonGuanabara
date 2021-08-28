from random import choices
from time import sleep


n=str(input('Primeiro nome: '))
n1=str(input('Segundo nome: '))
n2=str(input('Terceiro nome: '))
n3=str(input('Quarto nome: '))
lista=[n,n1,n2,n3]
escolhido=choices(lista)
print('\033[33mProcessando\033[m')
sleep(8)

print('O nome escolhido é {}'.format(escolhido))