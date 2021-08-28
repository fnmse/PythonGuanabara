n=str(input('Nome da pessoa: ')).strip()
n1=n.upper()
print(n1)
n2=n.lower()
print(n2)
n3=len(n)-n.count(' ')
print(n3)
separa=n.split()
print(separa)
print('O primeiro nome é {} e tem {} letras'.format(separa[0],len(separa[0])))


