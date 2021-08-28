from datetime import date
a=date.today().year
n=int(input('Qual ano do seu nascimento: '))
idade=a-n
#print(' Você tem {} anos em {}'.format(idade,a))
if idade==18:
    print('Você tem \033[34m{} anos,\033[m tem que fazer o alistamento'.format(idade))
elif idade<18:
    s=18-idade
    print ('Você tem \033[34m{} anos\033[m e falta \033[31m{} anos\033[m para se alistar'.format(idade,s))
else:
    s=idade-18
    print ('Você tem \033[34m {} anos \033[m e já passou \033[31m {} anos \033[m do seu alistamento '.format(idade,s))