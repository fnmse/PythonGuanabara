from time import sleep
n1=int(input('Digite um valor: '))
n2=int(input('Digite outro valor: '))
n=0
while n!=5:
    print('''' Segue as orientações abaixo: 
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS VALORES
    [5] SAIR DO PROGRAMA
''')
    n=int(input('Qual opçao vc escolhe? '))
    if n==1:
        print(n1+n2)
    elif n==2:
        print(n1*n2)
    elif n==3:
        maior=n
        if n2>n1:
            maior=n2
            print('O maior número entre {} e {} é {}'.format(n1,n2,maior))
    elif n==4:
        s=int(input('Digite outro número'))
    elif n==5:
        print('Finalizando...')
        sleep(2)
print(('fim'))





