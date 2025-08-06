import random

n1 = random.randint(0,10)
n2 = random.randint(0,10)
n3 = random.randint(0,10)
n4 = random.randint(0,10)
tupla = (n1,n2,n3,n4)
for c in range(0,4):
    print(f'{c+1}° - {tupla[c]}')

maior = 0
menor = 0
for pos in range(0,len(tupla)):
    if tupla[pos] >= maior:
        maior=tupla[pos]
    if tupla[pos] <= menor:
        menor=tupla[pos]
print(f'maior é {maior}\nmenor é {menor}')