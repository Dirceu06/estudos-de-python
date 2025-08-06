price = int(input('qual o preço? '))
desc = float(input('disconto de quanto? '))
print('o novo preço com {}% de desconto é {}'.format(desc,price-(price*(desc/100))))