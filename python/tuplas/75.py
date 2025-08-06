numLista = [0,0,0,0]
pares=0
for c in range(0,4):
    numLista[c]= int(input(f'{c+1}° número: '))
    if numLista[c]%2==0: pares=1

num = (numLista[0],numLista[1],numLista[2],numLista[3])
#num = (int(input('número: ')),int(input('número: ')),int(input('número: ')),int(input('número: ')))

print(f'o numero 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'o 3 apareceu na posição {num.index(3)+1}')
else:
    print('o 3 não apareceu')

if pares:
    print('valores pares digitados:',end='')
    for pos in range(0,4):
        if num[pos]%2==0: print(f' {num[pos]}',end='')
else: print('não houve pares digitados')