frase = input('frase: ').strip()
frase=''.join(frase.split())
aux=len(frase)-1
palindromo=1
for c in range(0,len(frase)):
    if frase[c]!=frase[aux-c]:
        print('não é palindromo')
        palindromo=0
        break
if palindromo:
    print('é palindromo')