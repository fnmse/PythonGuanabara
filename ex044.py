print('{:=^40}'.format('LOJAS FILIPE'))
p=float(input(' Digite o preço do produto:R$ '))
print('''Formas de pagamento:
[1] a vista dinheiro, 10% desconto
[2] a vista cartão, 5% desconto
[3] em até 2x cartão, perço normal
[4] 3x ou mais, 20% de juros''')
opçao=int(input('Digite a opção: '))
if opçao==1:
    p1=p- (p*0.10)
    print('Com desconto de 10% o valor do  produto será de R${:.2f}'.format(p1))
elif opçao==2:
    p1=p-(p*0.05)
    print(' Com desconto de 5% o valor do produto será de R${:.2f}'.format(p1))
elif opçao==3:
    p1=p
    print(' Em até 2x no cartão o preço será de R${:.2f}'.format(p))
else:
    p1=p+(p*0.20)
    print(' Em 3x ou mais o valor do produto será de R${:.2f}'.format(p1))

