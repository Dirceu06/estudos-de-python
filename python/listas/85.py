num = [[],[]]
for i in range(0,7):
    n = int(input(f'{i+1}° número: '))
    if n%2==0: num[0].append(n)
    else: num[1].append(n)
print(f'valores pares: {num[0]}\nimpares: {num[1]}')