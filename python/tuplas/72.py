extenso = ('um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze',
           'treze','quatorze','quinze','dezeseis','dezesete','dezoito','dezenove','vinte')

while True:
    n = int(input('numero: '))
    if n <= 20 and n >=1:
        break
    print('ENTRE 1 E 20, TENTE NOVAMENTE')
print(extenso[n-1])