n = int(input('quantos digitos deseja ver? '))
primeiro = 0
segundo = 1
firt = 1
while n!=0:
    if firt:
        print(primeiro,end='->')
        firt = 0
    aux=segundo
    print(segundo, end='')
    segundo = primeiro + segundo
    primeiro = aux
    n-=1
    if n != 0:
        print('->', end='')