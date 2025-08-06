def fatorial(num,show=False):
    """calcula o fatorial de um numero

    Args:
        num (int): numero que terá o fatorial calculado
        show (bool, optional): define se irá exibir o processo. Defaults to False.
    """
    fat=1
    for i in range(num,0,-1):
        fat*=i
        if show: 
            print(f'{i} ',end='')
            if i-1!=0: print('x ',end='')
            else: print(f'= ',end='')
    print(f'{fat}')


n = int(input('fatorial de quantos? '))
fatorial(5,show=True)
help(fatorial)