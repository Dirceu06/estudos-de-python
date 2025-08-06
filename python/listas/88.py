import random
from time import sleep
tamanho=40
print('-'*tamanho)
print(f'{('JOGUE NA MEGA SENA'):^40}')
print('-'*tamanho)
qtsjg=int(input('quantos palpites você quer? '))
palpites=[]
for i in range(0,qtsjg):
    validos = 0
    numeros=[]
    while True:
        n = random.randint(1,60)
        if n not in numeros: 
            numeros.append(n)
            validos+=1
        if validos==6:
            break
    palpites.append(numeros)
for i in range(qtsjg):
    print(f'Jogo {i+1}: {sorted(palpites[i])}')
    sleep(1)