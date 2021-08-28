km=float(input('Quantos km o carro rodou? '))
d=int(input('Quantos dias ficou alugado? '))
print('Com esse {}Km rodados e essa quantidade de {} dias você pagará o total de R${:.2f}'.format(km,d,((km*0.15+d*60))))