n=''
c=0
s=0
while True:
    n=int(input('Digite um número inteiro: '))
    if n==999:
        break
    s+=n
    c+=1
print(f'Você digitou {c} números e a soma deu {s}.')