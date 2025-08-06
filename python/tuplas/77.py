palavras = ('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON','CURSO','GRATIS','ESTUDAR')
for c in range(0,len(palavras)):
    print(f'na palavra {palavras[c]} temos ',end='')
    for b in palavras[c]:
        if b.lower() in 'aeiou': print(f' {b}',end='')
    print('')