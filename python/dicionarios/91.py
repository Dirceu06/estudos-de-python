import random
import time
from operator import itemgetter
jogadores = {}
for i in range(4):
    v = random.randint(1,6)
    jogadores[f'j{i+1}']=v
rank = dict()
rank = sorted(jogadores.items(),key=itemgetter(1),reverse=True)

# A CHAVE DESSE EXERCICIOS FOI O ITEMGETTER(1) ELE FALA PARA O SORTED QUE É PARA 
# ORGINZAR COM BASE NO VALORES '(1)', SE QUISER COM BASE NA POSIÇÃO '(0)'

i=1
for p,v in rank:
    print(f'{i}° lugar: {p} com {v} pontos')
    i+=1