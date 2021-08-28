from random import randint
while True:
    jogador=int(input('Digite um número: '))
    pc = randint(1, 20)
    total= jogador+pc
    r=' '
    while r not in 'PI':
        r=str(input('Par ou Ímpar: [P/I]')) .upper().strip()
    if r== 'P':
        if total%2==0:
            print (f' Você ganhou! Eu escolhi {pc} e vc {jogador} que somando fica em {total} que é par')
        else:
            print(f'Perdeu! A soma deu {total} que é ímpar')
    if r== 'i':
        if total%2>=0:
            print(f'Você ganhou! Eu escolhi {pc} e vc {jogador} que somando fica em {total} que é ímpar')
        else:
            print(f'Você perdeu! A soma deu {total} que é ímpar')





