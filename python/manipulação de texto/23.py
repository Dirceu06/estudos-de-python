import math
numero = int(input('digite um numero: '))

milhar = math.floor(numero/1000)
centena = math.floor((numero-milhar*1000)/100)
dezena = math.floor((numero-milhar*1000-centena*100)/10)
unidade = math.floor(numero-milhar*1000-centena*100-dezena*10)

print('unidade: {}\ndezena: {}\ncentena: {}\nmilhar: {}'.format(unidade,dezena,centena,milhar))