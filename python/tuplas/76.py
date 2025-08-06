listaCompras = ('Pão',1.5,'manteiga',9,'mortandela',5,'pão de alho',12,'pc gamer',120)
n = 11
print('='*n,'LISTA','='*n)
for c in range(0,len(listaCompras),2):
    print(f'{listaCompras[c]:.<20}R${listaCompras[c+1]:>7.2f}')
print('='*(2*n+7))