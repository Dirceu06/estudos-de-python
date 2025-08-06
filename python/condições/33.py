n1 = int(input('numero 1: '))
n2 = int(input('numero 2: '))
if n2 > n1:
    maior = n2
    menor = n1
else:
    maior = n1
    menor = n2
n3 = int(input('numero 3: '))

if n3 >= maior:
    maior = n3
if n3 < menor:
    menor = n3

print('maior: {}\nmenor: {}'.format(maior,menor))
