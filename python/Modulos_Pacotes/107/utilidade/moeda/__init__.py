def metade(num,format=False): 
    volta = ''
    num = num/2
    if format: volta = f'${num:.2f}'
    else: volta = f'{num}'
    return volta 

def dobro(num,format=False): 
    volta = ''
    num = num*2
    if format: volta = f'${num:.2f}'
    else: volta = f'{num}'
    return volta

def aumento(num,qtd,format=False):
    volta = ''
    num = num+(num*qtd/100)
    if format: volta = f'${num:.2f}'
    else: volta = f'{num}'
    return volta

def diminuir(num,qtd,format=False):
    volta = ''
    num = num-(num*qtd/100)
    if format: volta = f'${num:.2f}'
    else: volta = f'{num}'
    return volta

def money(num):
    return f'${num:.2f}'

def resumo(num,increase,decrease):
    print('-='*17,end='-\n')
    print(f'{('RESUMO DO VALOR'):^35}')
    print('-='*17,end='-\n')
    print(f'Preço analisado: {money(num):>17}')
    print(f'Dobro do preço: {dobro(num,True):>18}')
    print(f'Metade do preço: {metade(num,True):>17}')
    print(f'{increase}% de aumento: {aumento(num,increase,True):>18}')
    print(f'{decrease}% de reducao: {diminuir(num,decrease,True):>18}')
    