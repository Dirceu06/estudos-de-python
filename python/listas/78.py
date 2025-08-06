num = []
for c in range(0,5):
    while True:
        n = input(f'{c+1}° número: ')
        if n.isnumeric():
            break
    num.append(int(n))
numO = sorted(num,reverse=True)
maior=numO[0]
print(f'{maior} é o maior e está nas posições',end='')
for i in range(0,len(num)):
    if maior == num[i]: print(f' {i}',end='')

menor=numO[-1]
print()
print(f'{menor} é o menor e está nas posições',end='')
for i in range(0,len(num)):
    if menor == num[i]: print(f' {i}', end='')

#print(f'{maior} é o maior e está na posição {posMaior}\n{menor} é o menor e está na posição {posMenor}')