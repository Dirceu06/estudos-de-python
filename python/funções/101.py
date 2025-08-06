import datetime
def voto(ano):
    situacao = ''
    idade = datetime.datetime.now().year - ano
    if (idade >= 16 and idade < 18) or idade >=65: situacao = 'OPCIONAL'
    if idade >= 18: situacao = 'OBRIGATÓRIO'
    if idade < 16: situacao = 'NEGADO'
    return situacao


print(f'seu voto é {voto(int(input('ano de nascimento: ')))}')