import random
num = random.randint(0,5)
chute = int(input('qual seu chute?\nR:{}  '.format(num)))
if chute == num:
    print('acertou!!!!!')
else:
    print('errou!!!!!')