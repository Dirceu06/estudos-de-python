from datetime import datetime
ano_atual = datetime.now().year

cadastro = {}

cadastro['nome'] = input('nome: ')
ano_nasc = int(input('ano de nascimento: '))
cadastro['idade'] = ano_atual - ano_nasc
cadastro['ctps'] = int(input('carteira de trabalho (0 não tem): '))

if cadastro['ctps'] != 0:
    cadastro['contratado'] = int(input('ano da contratação: '))
    cadastro['salario'] = int(input('salário: '))

    cadastro['aposentadoria'] = (cadastro['contratado'] - ano_nasc) + 35 

for p,c in cadastro.items():
    print(f'{p} tem {c}')