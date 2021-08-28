n=''
r=str(['s/n'])
media=0
cont=0
soma=0
maior=0
menor=0
while r not in 'nN':
    n=int(input('Digite um número: '))
    r=str(input('Quer continuar? [s/n]:')).upper().strip()
    soma+=n
    cont+=1
medianum=soma/cont
print('A média dos números digitados é {:.2f}'.format(medianum))



