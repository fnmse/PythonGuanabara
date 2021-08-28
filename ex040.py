n1=float(input('Digite sua primeira nota: '))
n2=float(input('Digite sua segunda nota: '))
if (n1+n2)/2 <= 5:
    print('\033[31mreprovado\033[m')
elif (n1+n2)/2<=6.9:
    print('\033[33mRecuperação\033[m')
else:
    print('\033[34mAprovado\033[m')