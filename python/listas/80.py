num = []
for digitos in range(0,4):
    n = int(input(f'{digitos+1}°: '))
    if len(num)==0:
        pos = 0
    else:
        for c in range(0,len(num)):
            if n <= num[c]:
                pos=c
                break
            if c+1==len(num):
                pos = len(num)
                break
    num.insert(pos,n)

print(num)

