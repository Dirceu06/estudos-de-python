import os
os.system('cls')

report = {}
nome = input('Nome do jogador: ')
report['nome']=nome.capitalize()

qtdPart = int(input(f'Quantas partidas {report['nome']} jogou? '))
totGol=0
gols=list()
for p in range(qtdPart):
    gol = int(input(f'Quantos gols na {p} partida? '))
    totGol+=gol
    gols.append(gol)

report['gols']=gols[:]
report['total']=totGol

print('-='*30)

print(report)

print('-='*30)

for p,v in report.items():
    print(f'O campo {p} temos {v}')

print('-='*30)

print(f'O {report['nome']} jogou {qtdPart} partidas')
for p,v in enumerate(report['gols']):
    print(f'    => Na partida {p}, fez {v} gols')