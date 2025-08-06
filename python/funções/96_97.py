def area_ret():
    largura = int(input('Largura (m): '))
    altura = int(input('Altura (m): '))
    return largura*altura

#97
def cabecalho(msg):
    print('-'*int(len(msg)+2))
    print(f'{msg:^{len(msg)+2}}')
    print('-'*int(len(msg)+2))

cabecalho('aoo galera de peao')
area=area_ret()
print(f'Área do seu terreno é de {area}m²')