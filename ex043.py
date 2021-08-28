peso=float(input(' Digite seu peso: '))
al=float(input(' Digite sua altura: '))
imc=peso/(al*al)
if imc<18.5:
    print(' Seu imc é {:.1f}. Você está baixo do peso normal.'.format(imc))
elif imc<25:
    print(' Seu imc é {:.1f}. Você está no peso ideal.'.format(imc))
elif imc<30:
    print(' Seu imc é {:.1f}. Você está com sobrepeso'.format(imc))
elif imc<40:
    print(' Seu imc é {:.1f}. Você está com obesidade.'.format(imc))
else:
    print('Seu imc é {:.1f}.Você está com obesidade mórbida'.format(imc))