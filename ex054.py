from datetime import date
a=date.today().year
totalmaior=0
totalmenor=0
for c in range (1,8):
    n=int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    if a-n>=18:
        totalmaior+=1
    elif a-n<18:
         totalmenor+=1
print('Existem {} pessoas maiores de idade'.format(totalmaior))
print('Existem {} pessoas menores de idade'.format(totalmenor))


