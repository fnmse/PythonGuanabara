from datetime import date
n=int(input('Qual ano do seu nascimento: '))
a=date.today().year
i=a-n
if i<=9:
    print('O atleta tem {} anos, portanto, é da categoria \033[33mMIRIM\033[m'.format(i))
elif i<=14:
    print('O atleta tem {} anos, portanto, categoria \033[33mINFANTIL\033[m'.format(i))
elif i<=19:
    print('O atleta tem{} anos, portanto, é da categoria \033[33mJÙNIOR\033[m'.format(i))
elif i<=25:
    print(' O atleta tem {} anos, portanto, é da categoria \033[33mSênior\033[m'.format(i))
else:
    print('O atleta tem {} anos, portanto, é da categoria \033[33mMASTER\033[m'.format(i))
