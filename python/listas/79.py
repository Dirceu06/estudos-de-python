sair = 0
lista = []
while not sair:
    while True:
        n = input(f'número: ')
        if n.isnumeric(): break
        else: print('DIGITE UM NÚMERO')
    if n in lista: print('já esta na lista') 
    else: lista.append(int(n))

    while True:
        escolha = input('deseja continuar? [S/N] ')
        if escolha.upper() == 'S': break
        elif escolha.upper() == 'N': 
            sair=1 
            break
        else: print('resposta não interpretavél')

print(sorted(lista))