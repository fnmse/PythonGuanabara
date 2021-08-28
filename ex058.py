from random import randint
pc=randint(0,10)
print(pc)
usuario=''
soma=0
t=0
while usuario!=pc:
    usuario = int(input('Qual número eu pensei: '))
    soma+=1
    if usuario==pc:
        print('Parabéns! Você acertou. Foram necessárias {} tentativas'.format(soma))
    else:
        print('Você errou.Eu pensei no número {}'.format(pc))
print('fim')