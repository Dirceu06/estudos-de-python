idadeMedia = 0
Mulhervinte = 0
olderMan = 0
NameOlderMan='N/A'
for c in range(0,4):
    nome = input('{}° pessoa.nome: '.format(c+1))
    idade = int(input('{}° pessoa.idade: '.format(c+1)))
    sexo = input('{}° pessoa.sexo: (M/F) '.format(c+1)).upper()
    if sexo == 'M' and idade>olderMan:
        NameOlderMan = nome
        olderMan=idade
    idadeMedia = idadeMedia + idade
    if sexo == 'F' and idade < 20:
        Mulhervinte+=1
print('a media de idade foi {}\n{} é o homem mais velho\n{} mulhere(s) tem menos de 20 anos'.format(idadeMedia/4,NameOlderMan,Mulhervinte))