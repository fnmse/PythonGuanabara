somaidade=0
mediaidade=0
maior=0
nome=' '
for c in range (1,5):
    print('--------{}ª pessoa ------.'.format(c))
    n=str(input('Digite o nome: '.format(c)))
    idade=int(input('Digite a idade: '.format(c)))
    sexo=str(input('Sexo [M/F]:  '.format(c))).strip()
    somaidade+=idade
    if c==1 and sexo in 'Mm':
        maior=idade
        nome=n
    else:
        if sexo in 'Mm' and idade>maior:
            maior=idade
            nome=n
mediaidade=somaidade/4
print(' A média de idade é {}'.format(mediaidade))
print(' O homem mais velho tem {} anos e se chama {}'.format(maior,nome))

