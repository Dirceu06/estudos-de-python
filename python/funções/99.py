def maior(*num):
    maior=num[0]
    for n in num:
        if n>=maior: maior=n
    print(f'O maior é {maior}!!!')

maior(4,1,5,1,7,9,2342,6,53,13,31423,45)