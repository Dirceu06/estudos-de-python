def leiaInt(frase):
    while True:
        tentativa = input(frase)
        if tentativa.isnumeric(): break
    return tentativa    

n = leiaInt('digite um numero: ')
print('você digitou um número !!!')