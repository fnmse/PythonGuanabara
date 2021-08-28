soma=0
contmais=0
barato=' '
n=' '
cont=0
menor=0
while True:
    nome=str(input(' Nome do produto: '))
    preço=float(input('Preço do produto: R$'))
    r=str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    soma+=preço
    cont+=1
    menor+=1
    if preço>1000:
        contmais+=1
    if cont==preço:
        menor=preço
        n=nome
    elif preço<menor:
        menor=preço
        n=nome

    if r=='N':
        print('{:-^40}'.format('RESUMO DA COMPRA'))
        print(f'A soma dos produtos é {soma:.2f}')
        print(f'Existem {contmais} produtos que custam mais de $1.000,00')
        print(f'O produto mais barato é {n} que custa {preço:.2f}')
        print('{:-^40}'.format ('FIM DO PROGRAMA.'))
        break
