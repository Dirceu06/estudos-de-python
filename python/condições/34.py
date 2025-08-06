n1 = int(input('numero 1: '))
n2 = int(input('numero 2: '))
n3 = int(input('numero 3: '))
if n1 < n2+n3 and n2<n1+n3 and n3<n1+n2:
    print('é possivel o triangulo')
else:
    print('não é possivel o triangulo')