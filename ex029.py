n=float(input('Digite a velocidade em km: '))
if n>80:
    print('A sua velocidade foi {}km. Você foi multado em\033[31m R${:.2f}\033[m'.format(n,((n-80)*(7))))
else:
    print(' A sua velocidade foi de {}. Ótima viagem!'.format(n))
