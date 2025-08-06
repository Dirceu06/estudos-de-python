registro = {}
registro['nome'] = input('nome: ')
registro['media'] = int(input('media: '))
if registro['media'] < 6: registro['situacao'] = 'reprovado'
else: registro['situacao'] = 'aprovado'
for pos,valor in registro.items():
    print(f'Em {pos} temos {valor}')