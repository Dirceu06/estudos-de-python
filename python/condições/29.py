velocidade = int(input('qual a velocidade? '))
if velocidade > 80:
    print('ta rapido em irmão paga ai R${:.2f} para o governo'.format(7*(velocidade-80)))
else:
    print('boa garoto continua assim')