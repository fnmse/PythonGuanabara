from random import randint
while True:
    jogador=int(input('Digite um valor:'))
    computador=randint(0,10)
    total= jogador + computador
    tipo=' '
    while tipo not in 'PI':
        tipo=str(input(' vc escolhe Par ou Ímpar:')).strip().upper()[0]
    print(f'Jogador jogou {jogador} e computador jogou {computador}.A soma deu {total}.')
    if tipo=='P':
        if total%2==0:
            print(f'Jogador ganhou. A soma deu {total} que é par.')

        else:
            print(f'Você perdeu! {total} é ímpar.')
            break
    elif tipo=='I':
        if total%2==1:
            print(f'Você venceu.{total} é ímpar.')
        else:
            print(f'Você perdeu. A soma deu {total} que é par.' )
            break

