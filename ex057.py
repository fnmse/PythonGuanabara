sexo=str('[M/F')
while sexo not in 'M' and sexo not in'F':
    sexo=str(input('Digite seu sexo [M/F]: ')).upper()
    if sexo=='M':
        print('Você é do sexo masculino.')
    elif sexo=='F':
        print('Você é do sexo feminino')
    else:
        print('Digite seu sexo corretamente!')
