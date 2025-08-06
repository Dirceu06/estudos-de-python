import time
def a():
    print('-'*30)
    print(f'{'1 a 10, pulando 1':^30}')
    print('-'*30)
    for i in range(10):
        print(f'{i+1} ',end='',flush=True)
        time.sleep(0.2)
    print('\nFIM')

def b():
    print('-'*30)
    print(f'{'10 a 0, pulando 2':^30}')
    print('-'*30)
    for j in range(10,0,-2):
        print(f'{j} ',end='',flush=True)
        time.sleep(0.2)
    print('\nFIM')
    

def c():
    print('-'*30)
    print(f'{'agora é sua vez !!!':^30}')
    print('-'*30)
    inicio = int(input('inicio: '))
    fim = int(input('fim: '))
    pulos = int(input('pulos: '))

    if pulos==0: pulos=1
    if inicio < fim and pulos < 0: pulos = -pulos
    if inicio > fim and pulos > 0: pulos = -pulos

    print(f'Iniciando em {inicio} para terminar em {fim} pulando {abs(pulos)}')

    for i in range(inicio,fim,pulos):
        print(f'{i} ',end='',flush=True)
        time.sleep(0.2)
    print('\nFIM')


a()  
b()
c()