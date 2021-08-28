n=''
cont=0
soma=0
while n!=999:
    n=int(input('Digite um numero: '))
    cont+=1
    soma+=n
if n==999:
    print(' Você digitou {} numeros e a soma desse numeros deu {}.'.format(cont,soma-999))
print('FIM')