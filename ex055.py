maior=0
menor=0
for peso in range(1,6):
    p=float(input('Peso da {}ª pessoas: '.format(peso)))
    if p==1:
        maior=peso
        menor=peso
    else:
        if p>maior:
            maior=p
        if p<menor:
            menor=p
print('O maior peso é {}'.format(maior))
print('O menor peso é {}'.format(menor))