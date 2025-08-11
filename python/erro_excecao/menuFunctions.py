import ex113
import sys

def main_menu():
    print('-'*30)
    print(f'{('MENU PRINCIPAL'):^30}')
    print('-'*30)
    print('1 - Ver pessoas cadastradas\n2 - Cadastrar uma nova pessoa\n3 - Sair do sistema')
    print('-'*30)
    while True:
        escolha = ex113.leiaInt('Sua escolha: ')
        if escolha >= 1 and escolha <=3: break
        else: print('Não existe essa opção')
    return escolha

def verPessoas():
    print('-'*30)
    try:
        with open('dados.txt', 'r', encoding='utf-8') as f:
            for linha in f:
                nome, idade = linha.strip().split(',')
                print(f'{nome.strip():<20}{(f'{idade.strip()} anos'):>10}')
    except FileNotFoundError:
        print('Não há pessoas ou arquivo de texto para ser lido')

def cadPessoas():
    print('-'*30)
    nome = input('Nome: ')
    idade = ex113.leiaInt('Idade: ')
    try: 
        with open('dados.txt','a',encoding='utf-8') as f:
            f.write(f'{nome}, {idade}\n')
    except FileNotFoundError: 
        with open('dados.txt','w',encoding='utf-8') as f:
            f.write(f'{nome}, {idade}\n')
    
def sair():
    sys.exit()