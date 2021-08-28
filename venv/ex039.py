ano=int(input('Qual ano do seu nascimento? '))
idade=2021-ano
t=idade-18
if idade==18:
    print('Você tem {} anos, portanto, está no ano do seu alistamento!'.format(idade))
elif idade<=18:
    print('Você tem {} anos. Faltam {} anos para seu alistamento'.format(idade,t))
elif idade>18:
    print('Você tem {} anos. Já passou {} anos do seu alistamento.'.format(idade,t))