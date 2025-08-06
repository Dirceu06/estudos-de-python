import random
def sorteia(lst):
    for i in range(5):
        lst.append(random.randint(0,10))
    print(lst)

def somaPar(lst):
    pos = 0
    s = 0
    while pos < len(lst):
        if lst[pos]%2==0: s+=lst[pos]
        pos+=1
    print(f'O resultado da soma dos pares é {s}')


lista = list()
sorteia(lista)
somaPar(lista)