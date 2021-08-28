f=str(input('Digite uma frase:')).strip().upper()
f1=f.split()
j=''.join(f1)
inverso=j[::-1]
print('O inverso de {} é {}.'.format(j,inverso))
if inverso==j:
    print('Temos um Polídromo!')
else:
    print('Não temos um Polídromo!')