import menuFunctions
import os

# Windows
if os.name == 'nt':
    os.system('cls')
# Linux / macOS
else:
    os.system('clear')

while True:
    escolha = menuFunctions.main_menu()
    if escolha == 1: menuFunctions.verPessoas()
    if escolha == 2: menuFunctions.cadPessoas()
    if escolha == 3: menuFunctions.sair()