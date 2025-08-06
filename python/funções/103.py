def ficha(nome='desconhecido',gols=0):
    if nome == '': nome = 'desconhecido'
    if gols == '': gols=0
    print(f'o jogador {nome} fez {gols} gol(s)')

n = input('nome do jogador: ')
gol = input('gols do jogador: ')
ficha(n,gol)