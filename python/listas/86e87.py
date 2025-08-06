matriz = []
for i in range(0,3):
    linha = []
    for j in range(3):
        linha.append(int(input(f'linha {i} e coluna {j}: ')))
    matriz.append(linha)
for k in range(0,3):
    print(f'{matriz[k]}')

#soma de todos os elementos
s=0
for i in range(3):
    for j in range(3):
        s=s+matriz[i][j]
print(f'A soma de todos resulta em {s}')

#soma de todos da terceira coluna //[2]
sT=0
for i in range(3):
    sT=sT+matriz[i][2]
print(f'A soma da terceira coluna resulta em {sT}')

#O maior da segunda linha
maior=matriz[1][0]
for i in range(3):
    if matriz[1][i] > maior: maior = matriz[1][i]
print(f'O maior valor da segunda linha é {maior}') 