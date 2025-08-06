turma = list()
notas = list()
i=0
while True:
    i+=1
    nome = input(f'qual o nome do aluno {i}: ')
    notas.append(int(input('qual a nota 1: ')))
    notas.append(int(input('qual a nota 2: ')))
    turma.append([nome,notas[:]])
    notas.clear()
    
    r = input('deseja continuar? [S/N] ')
    if r.upper() == 'N':
        break
#TABELA

print('| {:^3} | {:^8} | {:^6} | {:^6} | {:^6} |'.format(('N°'),('nome'),('Nota 1'),('Nota 2'),('Média')))
for j in range(len(turma)):
    print('| {:^3} | {:^8} | {:^6} | {:^6} | {:^6} |'.format(j,turma[j][0],turma[j][1][0],turma[j][1][1],(turma[j][1][1]+turma[j][1][0])/2))

while True:
    n1 = int(input('qual aluno deseja ver? (999 interronper) '))
    if n1 == 999:
        break
    if n1 in range(0,len(turma)):
        print('| {:3} | {:^8} | {:^6} | {:^6} | {:^6} |'.format(n1,turma[n1][0],turma[n1][1][0],turma[n1][1][1],(turma[n1][1][1]+turma[n1][1][0])/2))
    else: print('aluno não encontrado')