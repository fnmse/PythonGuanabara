d=float(input('Digite a km da viagem: '))
v1=d*0.50
v2=d*0.45
if d<=200:
    print('A distância da sua viagem é {}. Você pagará R${:.2f}'.format(d,v1))
else:
    print('A distância da sua viagem é {}. Você pagará R${:.2f}'.format(d,v2))