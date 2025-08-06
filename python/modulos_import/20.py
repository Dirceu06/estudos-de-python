import random
grupos = ['perneta','desprovidos','belos','carismaticos']
posOcupadas = [-1,-1,-1,-1]
i = 0

while i < 4:
    pos=random.randint(0,3)
    i=i+1
    j=0
    while j < 4:
        if pos == posOcupadas[j]:
            i=i-1
        j=j+1
    posOcupadas[i]=pos
i = 0
while i < 4:
    print('{}° é {}'.format(i,grupos[posOcupadas[i]]))