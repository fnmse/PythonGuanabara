n=int(input('Digite um número para saber se ele é primo:'))
soma=0
for c in range(1,n+1):
    if n%c==0:
        print('\033[33m',end=' ')
        soma+=1
    else:
        print('\033[31m',end=' ')
    print(c,end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(n,soma))
if soma==2:
    print('Ele é primo')
else:
    print('Ele não é primo')