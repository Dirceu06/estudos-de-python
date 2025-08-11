def validacao():
    while True:
        tentativa = input('Valor: R$').replace(',','.').strip()
        if tentativa.isalpha(): print("\033[31mNão é um número\033[m")
        else: break
    return float(tentativa)
        
            