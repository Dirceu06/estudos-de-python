import os
os.system('cls')

pessoa = dict()
povo = list()
somaIdade=0
qtdPessoa=0
while True:

    pessoa['nome'] = (input('Nome: ')).capitalize()
    pessoa['sexo'] = (input('Sexo: [M/F] ')).upper()
    pessoa['idade'] = int(input('Idade: '))
    somaIdade+=pessoa['idade']
    qtdPessoa+=1
    povo.append(pessoa.copy())
    pessoa.clear()


    resposta = input('deseja continuar? [S/N] ')
    if(resposta.upper()=='N'): break

media = somaIdade/qtdPessoa
print('-='*30)
print(f'- O grupo tem {qtdPessoa} pessoa(s).')
print(f'- O grupo tem {media:.2f} como media de idade.')
print(f'- As mulheres no grupo são:',end='')
for p in range(qtdPessoa):
    if povo[p]['sexo']=='F': print(f' {povo[p]['nome']}',end='')
print('.')

print('lista das pessoas com idade maior que a media: ')
for p in range(qtdPessoa):
    if povo[p]['idade'] > media: print(f'- {povo[p]['nome']}, {povo[p]['idade']} anos.') 
