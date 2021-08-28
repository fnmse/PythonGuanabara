cont=0
soma=0
for c in range(1,7):
    n=int(input('Digite um número: '))
    if n%2==0:
        cont=cont+1
        soma=soma+n
print('A soma de {} valores é {}'.format(cont,soma))


