inicio = int(input('qual o primeiro numero da PA? '))
raz = int(input('qual a razão da PA? '))
i=inicio
for c in range(1,11):
    print('{}°: {}'.format(c,i))
    i=i+raz
