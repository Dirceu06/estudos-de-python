tupla = ('flamengo','cruzeiro','bragantino','palmeiras','bahia','fluminence','atletico-mg',
         'botafogo','chapecoense','corinthians')
#a
for c in range(1,6):
    print(f'| {c}° - {tupla[c-1]:^15} |')

print('-='*20)
pos = len(tupla)-5
for pos in range(pos,len(tupla)):
    print(f'| {pos+1}° - {tupla[pos]:^15} |')
ordenada = sorted(tupla)
print(ordenada)
print(f'a chapecoence está em {tupla.index('chapecoense')}°')