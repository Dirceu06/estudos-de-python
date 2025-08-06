pessoas = list()
individuo = list()
while True:
    nome = input('nome: ')
    peso = int(input('peso: '))
    individuo.append(nome)
    individuo.append(peso)
    pessoas.append(individuo[:])
    individuo.clear()

    r = input('deseja continuar? [S/N] ')
    if r.upper() == 'N':
        break

print(f'{len(pessoas)} pessoa(s) foram cadastradas')
pesos=list()
for p in range(0,len(pessoas)):
    if pessoas[p][1] not in pesos: pesos.append(pessoas[p][1])

print('_'*35)
print()
print(f'{('Pesos pesados'):^35}')
print('_'*35)

pesos = sorted(pesos,reverse=True)
for kg in range(0,len(pesos)):
    for p in range(0,len(pessoas)):
        if pessoas[p][1] == pesos[kg]:
            print(f'{pessoas[p][0]:.<20}{pesos[kg]:5.2f}Kg')

print('_'*35)
print()
print(f'{('Pesos pena'):^35}')
print('_'*35)

pesos = sorted(pesos)
for kg in range(0,len(pesos)):
    for p in range(0,len(pessoas)):
        if pessoas[p][1] == pesos[kg]:
            print(f'{pessoas[p][0]:.<20}{pesos[kg]:5.2f}Kg')