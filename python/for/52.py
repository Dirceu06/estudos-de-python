n = int(input('numero: '))
primo = 1
for c in range(2,n):
    if n%c==0:
        print('não é primo')
        primo = 0
        break
if primo:
    print('é primo')