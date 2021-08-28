sexo=' '
cont=0
maior=0
menor=0
r=' '
m=0
f=0
sexo2=' '
while True:
    idade=int(input('Digite sua idade: '))
    sexo=str(input('Digite seu sexo: ')).strip().upper()[0]
    r=str(input('Deseja continuar o cadastro? Sim ou Não? ')).strip().upper()[0]
    cont+=1
    if sexo in'mM':
        m+=1
    elif sexo in'fF':
        f+=1
        if idade<18:
            menor+=1
    if idade>=18:
        maior+=1
    if r not in 'sS':
        print(f'Existe {cont} cadastradas.Dessas {m} são do sexo masculino e {f} feminino.')
        print(f'Existem {maior} pessoas maiores de idade')
        print(f'Existem {menor} mulheres menor de idade.')
        break

