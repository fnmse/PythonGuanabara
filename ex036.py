v=float(input('Digite o valor da casa:R$ '))
s=float(input('Digite sua renda:R$ '))
f=int(input('Digite o tem de financiamento: '))
p=v/(f*12)
if p<=s*0.30:
    print('\033[33mO seu financiamento foi aprovado. O valor da prestação será de R${:.2f}\033[m'.format(p))
else:
    print('\033[31mFinanciamento reprovado\033[m')
