def leiaInt(msg):
    while True:
        try:
            num = input(msg).strip()
            num=int(num)
        except ValueError: 
            print(f'Isto não é um inteiro')
        except KeyboardInterrupt:
            print('O usuário prefiriu não digitar esse número')
            return 0
        else:
            return num
        
def leiaFloat(msg):
    while True:
        try:
            num = input(msg).strip()
            num=float(num)
        except ValueError: 
            print(f'Isto não é um número real')
        except KeyboardInterrupt:
            print('O usuário prefiriu não digitar esse número')
            return 0
        else:
            return num
    