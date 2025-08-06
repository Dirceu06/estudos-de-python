nome = input('frase: ')
nome = nome.strip()
qntA = nome.upper().count('A')
posA = nome.upper().find('A')
posAultimo = nome.upper().rfind('A')

print('quantidade de A: {}\nPosição do primeiro A: {}\nPosição do ultimo A: {}'.format(qntA,posA,posAultimo))