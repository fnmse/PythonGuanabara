
while True:
    n = int(input('DIGITE UM VALOR PARA SABER SUA TABUADA: '))
    if n<0:
        break
    for c in range (1,11):
        print(f'{n} * {c} = {n*c}')
print('Programa de tabuada encerrada')